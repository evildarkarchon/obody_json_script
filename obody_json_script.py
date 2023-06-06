import json

base = '''
{
    "raceFemale": {},
    "raceMale": {},
    "npc": {},
    "blacklistedNpcs": [],
    "blacklistedRaces": [
        "ElderRace"
    ],
    "blacklistedPresetsFromRandomDistribution": [
        "- Zeroed Sliders -",
        "-Zeroed Sliders-",
        "Zeroed Sliders"
    ],
    "blacklistedPresetsShowInOBodyMenu": false,
    "blacklistedOutfitsFromORefit": [],
    "outfitsForceRefit": []
}
'''

config = json.loads(base)

# Use python dictionary syntax to add or modify entries in the configuration file.

with open('OBody_presetDistributionConfig.json', 'w') as f:
    json.dump(config, f, indent=4, sort_keys=True)