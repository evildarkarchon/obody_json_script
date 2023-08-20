import json

base = '''
{
    "npcFormID": {},
    "npc": {},
    "factionFemale": {},
    "factionMale": {},
    "npcPluginFemale": {},
    "npcPluginMale": {},
    "raceFemale": {},
    "raceMale": {},
    "blacklistedNpcs": [],
    "blacklistedNpcsFormID": {},
    "blacklistedNpcsPluginFemale": [],
    "blacklistedNpcsPluginMale": [],
    "blacklistedRacesFemale": [
        "ElderRace"
    ],
    "blacklistedRacesMale": [
        "ElderRace"
    ],
    "blacklistedOutfitsFromORefitFormID": {},
    "blacklistedOutfitsFromORefit": [],
    "blacklistedOutfitsFromORefitPlugin": [],
    "outfitsForceRefitFormID": {},
    "outfitsForceRefit": [],
    "blacklistedPresetsFromRandomDistribution": [
        "- Zeroed Sliders -",
        "-Zeroed Sliders-",
        "Zeroed Sliders",
        "HIMBO Zero for OBody"
    ],
    "blacklistedPresetsShowInOBodyMenu": true
}

'''

config = json.loads(base)

# Use python dictionary syntax to add or modify entries in the configuration file.

with open('OBody_presetDistributionConfig.json', 'w') as f:
    json.dump(config, f, indent=4, sort_keys=True)