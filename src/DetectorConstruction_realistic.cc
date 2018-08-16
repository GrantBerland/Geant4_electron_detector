//
// ********************************************************************
// * License and Disclaimer                                           *
// *                                                                  *
// * The  Geant4 software  is  copyright of the Copyright Holders  of *
// * the Geant4 Collaboration.  It is provided  under  the terms  and *
// * conditions of the Geant4 Software License,  included in the file *
// * LICENSE and available at  http://cern.ch/geant4/license .  These *
// * include a list of copyright holders.                             *
// *                                                                  *
// * Neither the authors of this software system, nor their employing *
// * institutes,nor the agencies providing financial support for this *
// * work  make  any representation or  warranty, express or implied, *
// * regarding  this  software system or assume any liability for its *
// * use.  Please see the license in the file  LICENSE  and URL above *
// * for the full disclaimer and the limitation of liability.         *
// *                                                                  *
// * This  code  implementation is the result of  the  scientific and *
// * technical work of the GEANT4 collaboration.                      *
// * By using,  copying,  modifying or  distributing the software (or *
// * any work based  on the software)  you  agree  to acknowledge its *
// * use  in  resulting  scientific  publications,  and indicate your *
// * acceptance of all terms of the Geant4 Software license.          *
// ********************************************************************
//
// $Id: DetectorConstruction.cc 94307 2015-11-11 13:42:46Z gcosmo $
//
/// \file DetectorConstruction.cc
/// \brief Implementation of the DetectorConstruction class

#include "DetectorConstruction.hh"

#include "G4RunManager.hh"
#include "G4NistManager.hh"
#include "G4Box.hh"
#include "G4Cons.hh"
#include "G4Orb.hh"
#include "G4Sphere.hh"
#include "G4Trd.hh"
#include "G4LogicalVolume.hh"
#include "G4PVPlacement.hh"
#include "G4SystemOfUnits.hh"

//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......

DetectorConstruction::DetectorConstruction()
: G4VUserDetectorConstruction(),
  fScoringVolume(0)
{ }

//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......

DetectorConstruction::~DetectorConstruction()
{ }

//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......

G4VPhysicalVolume* DetectorConstruction::Construct()
{
  // Get nist material manager
  G4NistManager* nist = G4NistManager::Instance();

  // Envelope parameters
  //
  G4double env_sizeXY = 20*cm, env_sizeZ = 30*cm;
  // G4Material* env_mat = nist->FindOrBuildMaterial("G4_");

    // Material: Vacuum
    //TODO: check pressures, environment for Van Allen belt altitudes
  G4Material* env_mat = new G4Material("Vacuum",
              1.0 , 1.01*g/mole, 1.0E-25*g/cm3,
              kStateGas, 2.73*kelvin, 3.0E-18*pascal );

  // Option to switch on/off checking of volumes overlaps
  //
  G4bool checkOverlaps = true;

  //
  // World
  //
  G4double world_sizeXY = 1.2*env_sizeXY;
  G4double world_sizeZ  = 1.2*env_sizeZ;
  // G4Material* world_mat = nist->FindOrBuildMaterial("G4_AIR");
  G4Material* world_mat = new G4Material("Vacuum",
              1.0 , 1.01*g/mole, 1.0E-25*g/cm3,
              kStateGas, 2.73*kelvin, 3.0E-18*pascal );

  G4Box* solidWorld =
    new G4Box("World",                       //its name
       0.5*world_sizeXY, 0.5*world_sizeXY, 0.5*world_sizeZ);     //its size

  G4LogicalVolume* logicWorld =
    new G4LogicalVolume(solidWorld,          //its solid
                        world_mat,           //its material
                        "World");            //its name

  G4VPhysicalVolume* physWorld =
    new G4PVPlacement(0,                     //no rotation
                      G4ThreeVector(),       //at (0,0,0)
                      logicWorld,            //its logical volume
                      "World",               //its name
                      0,                     //its mother  volume
                      false,                 //no boolean operation
                      0,                     //copy number
                      checkOverlaps);        //overlaps checking

  //
  // Envelope
  //
  G4Box* solidEnv =
    new G4Box("Envelope",                    //its name
        0.5*env_sizeXY, 0.5*env_sizeXY, 0.5*env_sizeZ); //its size

  G4LogicalVolume* logicEnv =
    new G4LogicalVolume(solidEnv,            //its solid
                        env_mat,             //its material
                        "Envelope");         //its name

  new G4PVPlacement(0,                       //no rotation
                    G4ThreeVector(),         //at (0,0,0)
                    logicEnv,                //its logical volume
                    "Envelope",              //its name
                    logicWorld,              //its mother  volume
                    false,                   //no boolean operation
                    0,                       //copy number
                    checkOverlaps);          //overlaps checking


  //TODO: change these to reflect electron detector dimensions initial guess
  G4double detector_dimX = 10/2.*mm;
  G4double detector_dimY = 2.2/2.*mm;
  G4double detector_dimZ = 5./2.*mm;
  G4double baffle_thickness = 0.5/2.*mm;
  G4double baffle_height    = 20/2.*mm;

  G4int n_detectors = 2;


  // ----------------------------------------------------------------
  // Detector elements:
  // ----------------------------------------------------------------
  // G4Material* detector_mat = nist->FindOrBuildMaterial("G4_Si");

  // (Element name, symbol, atomic number, atomic mass) (as floats)
  G4Element* Si = new G4Element("Silicon","Si", 14., 28.0855*g/mole); // main waifer material for detector
  G4Element* S = new G4Element("Sulfer","S", 16., 32.065*g/mole);   // possible doping material
  //G4Element* B = new G4Element("Boron","B", 5., 10.811*g/mole);   // possible doping material

  G4Element* Ga = new G4Element("Gallium","Ga", 31., 69.723*g/mole);
  G4Element* As = new G4Element("Arsenic","As", 33., 74.9216*g/mole);

  // Gallium Arsenide to be used in doping the silicon detector wafers (is this the right way to do it?)
  G4Material* GalliumArsenide = new G4Material("GalliumArsenide", 5.32*g/cm3, 2);
  GalliumArsenide->AddElement(Ga, 50*perCent);
  GalliumArsenide->AddElement(As, 50*perCent);

  //G4Element* Be = new G4Element("Beryllium","Be", 4., 9.0122*g/mole);   // material for window

  // Final doped silicon material to be used in the electron detector
  G4Material* DopedSilicon = new G4Material("DopedSilicon", 5.8*g/cm3, 2); // last argument is ncomponents?
  DopedSilicon->AddElement(Si, 98*perCent);
  DopedSilicon->AddElement(S, 2*perCent);


  G4ThreeVector detector_pos  = G4ThreeVector(0, 0, 0);

  std::ostringstream detname;

  G4VSolid* detector_solid = new G4Box("detector",
                   detector_dimX, detector_dimY, detector_dimZ);

  // Generate the detector elements
  for (int i=1; i <= n_detectors; i++){
    detname.str("");
    detname << "detector" << i;

    detector_pos  = G4ThreeVector(0, 2*i*(detector_dimY), 0);

    G4LogicalVolume* detector =
    new G4LogicalVolume(detector_solid,      //its solid
                        DopedSilicon,        //its material
                        detname.str());      //its name

    new G4PVPlacement(0,                     //no rotation
                    detector_pos,            //at position
                    detector,                //its logical volume
                    detname.str(),           //its name
                    logicEnv,                //its mother  volume
                    false,                   //no boolean operation
                    0,                       //copy number
                    checkOverlaps);          //overlaps checking

  }

  // ----------------------------------------------------------------
  // Window
  // ----------------------------------------------------------------

  G4Material* window_material = nist->FindOrBuildMaterial("G4_Be");
  G4VSolid*   window_solid = new G4Box("window", detector_dimX, baffle_thickness,  baffle_height + detector_dimZ);

  G4ThreeVector window_pos;
  std::ostringstream window_name;

  // Creation of beryllium window to repel protons
  window_name.str("");
  window_name << "window" << 1;

  window_pos = G4ThreeVector(0, (2 + 1)*(detector_dimY + baffle_thickness),  baffle_height);

  G4LogicalVolume* window =
  new G4LogicalVolume(window_solid,         // its solid
                      window_material,      // its Material
                      window_name.str());    // its name

  new G4PVPlacement(0,                       //no rotation
                    window_pos,              //at position
                    window,                  //its logical volume
                    window_name.str(),       //its name
                    logicEnv,                //its mother  volume
                    false,                   //no boolean operation
                    0,                       //copy number
                    checkOverlaps);          //overlaps checking
/*
  // Generate baffles in between the detectors
  for (int i=-1*(n_detectors_left + 1); i <= n_detectors_right; i++) {
    baffle_name.str("");
    baffle_name << "baffle" << i;
    baffle_pos = G4ThreeVector(0, (2*i + 1)*(detector_dimY + baffle_thickness),  baffle_height);
    G4LogicalVolume* baffle =
    new G4LogicalVolume(baffle_solid,          //its solid
                          baffle_material,     //its material
                          baffle_name.str());  //its name

    new G4PVPlacement(0,                       //no rotation
                      baffle_pos,              //at position
                      baffle,                  //its logical volume
                      baffle_name.str(),       //its name
                      logicEnv,                //its mother  volume
                      false,                   //no boolean operation
                      0,                       //copy number
                      checkOverlaps);          //overlaps checking

  }
  // ----------------------------------------------------------------
*/
  //always return the physical World
  return physWorld;
}

//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......
