#include "G4VSensitiveDetector.hh"

class ElectronSensitiveDetector : public G4VSensitiveDetector
{
public:
    ElectronSensitiveDetector(G4String SDname);

    ~ElectronSensitiveDetector();


public:
    // Method called when particle passes through sensitive volume
    G4bool ProcessHits(G4Step *step, G4TouchableHistory *ROhist) = 0;

    // Optional init event action
    void Initialize(G4HCofThisEvent* HCE);

    // Optional end event action
    void EndOfEvent(G4HCofThisEvent* HCE);

private:
};
