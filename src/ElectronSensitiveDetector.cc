
#include "ElectronSensitiveDetector.hh"



G4bool ElectronSensitiveDetector::ProcessHits(G4Step *step, G4TouchableHistory *ROhist)
{
  // G4Track contains position, momentum, etc. info of particle to be queried
  G4Track* track = step->GetTrack();

  G4ThreeVector momentum = track->GetMomentumDirection();
  G4ThreeVector position = track->GetPosition();

  G4double position_x = position.x();
  G4double position_y = position.y();
  G4double position_z = position.z();

  G4double mom_x = momentum.x();
  G4double mom_y = momentum.y();
  G4double mom_z = momentum.z();
  G4double mom_mag = sqrt(pow(mom_x, 2)+pow(mom_y, 2)+pow(mom_z, 2));

  G4double angle_x = acos(mom_x/mom_mag);
  G4double angle_y = acos(mom_y/mom_mag);
  G4double angle_z = acos(mom_z/mom_mag);

}

void ElectronSensitiveDetector::Initialize(G4HCofThisEvent* HCE){}
void ElectronSensitiveDetector::EndOfEvent(G4HCofThisEvent* HCE){}
