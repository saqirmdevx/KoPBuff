z = """import { Shared } from './types';

const getItemStats = (itemId: Shared.ItemList, itemData: Shared.IItemData): void => {
    switch (itemId) {
    case Shared.ItemList.Wooden_Sword:
        itemData.displayId = 'WoodenSword';
        itemData.bonusStats = { damage: 6 };
        break;
    case Shared.ItemList.Wooden_Bow:
        itemData.displayId = 'WoodenBow';
        itemData.bonusStats = { attackSpeed: 0.12 };
        break;
    case Shared.ItemList.Buckler:
        itemData.displayId = 'Buckler';
        itemData.bonusStats = { armor: 2 };
        break;
    case Shared.ItemList.Novice_Staff:
        itemData.displayId = 'NoviceStaff';
        itemData.bonusStats = { abilityPower: 15 };
        break;
    case Shared.ItemList.Iron_Ring:
        itemData.displayId = 'IronRing';
        itemData.cost = 150;
        itemData.bonusStats = { hpRegen: 2 };
        break;
    case Shared.ItemList.Boots:
        itemData.displayId = 'Boots';
        itemData.bonusStats = { moveSpeed: 5 };
        itemData.isBootsType = true;
        itemData.cost = 150;
        break;
    case Shared.ItemList.Shirt:
        itemData.displayId = 'Shirt';
        itemData.cost = 150;
        itemData.bonusStats = { maxHealth: 60 };
        break;

        /** Consumables */
    case Shared.ItemList.Healing_Potion:
        itemData.displayId = 'HealingPotion';
        itemData.cost = 50;
        itemData.isConsumable = true;
        itemData.isUsable = true;
        break;

    case Shared.ItemList.Observer_Ward:
        itemData.displayId = 'Ward';
        itemData.cost = 20;
        itemData.isConsumable = true;
        itemData.isUsable = true;
        break;

    case Shared.ItemList.Sentry_Ward:
        itemData.displayId = 'WardRed';
        itemData.cost = 50;
        itemData.isConsumable = true;
        itemData.isUsable = true;
        break;

    case Shared.ItemList.Corrupted_Potion:
        itemData.displayId = 'CorruptedPotion';
        itemData.cost = 450;
        itemData.isConsumable = true;
        itemData.isUsable = true;
        break;

    case Shared.ItemList.Potion_Of_Magic:
        itemData.displayId = 'PotionOfMagic';
        itemData.cost = 450;
        itemData.isConsumable = true;
        itemData.isUsable = true;
        break;

        /** Tier 2 */
        /** Wooden Sword */
    case Shared.ItemList.Light_Slayer:
        itemData.displayId = 'LightSlayer';
        itemData.cost = 300;
        itemData.bonusStats = {
            damage: 13,
            attackSpeed: 0.12
        };
        itemData.parentItemId = Shared.ItemList.Wooden_Sword;
        break;

        /** Tier 3 - Light Slayer */
    case Shared.ItemList.Corrupted_Light_Slayer:
        itemData.displayId = 'CorruptedLightSlayer';
        itemData.cost = 600;
        itemData.bonusStats = {
            attackSpeed: 0.2,
            damage: 15,
            lifesteal: 0.2,
        };
        itemData.parentItemId = Shared.ItemList.Light_Slayer;
        itemData.isUsable = true;
        break;

    case Shared.ItemList.Katana:
        itemData.displayId = 'Katana';
        itemData.cost = 450;
        itemData.bonusStats = {
            damage: 18,
        };
        itemData.parentItemId = Shared.ItemList.Wooden_Sword;
        break;

    case Shared.ItemList.Shadow_Slayer:
        itemData.displayId = 'ShadowSlayer';
        itemData.cost = 550;
        itemData.bonusStats = {
            attackSpeed: 0.35,
        };
        itemData.innerCooldown = 100;
        itemData.parentItemId = Shared.ItemList.Light_Slayer;
        break;

    case Shared.ItemList.Corrupted_Katana:
        itemData.displayId = 'CorruptedKatana';
        itemData.cost = 600;
        itemData.bonusStats = {
            damage: 20,
            criticalChance: 0.35
        };
        itemData.parentItemId = Shared.ItemList.Katana;
        break;

    case Shared.ItemList.Divine_Katana:
        itemData.displayId = 'DivineKatana';
        itemData.cost = 475;
        itemData.bonusStats = { 
            damage: 20, 
            cooldownReduction: 0.1, 
            lifesteal: 0.1
        };
        itemData.parentItemId = Shared.ItemList.Katana;
        itemData.isUsable = true;
        break;

    case Shared.ItemList.Iron_Sword:
        itemData.displayId = 'IronSword';
        itemData.cost = 300;
        itemData.bonusStats = {
            damage: 9,
            maxHealth: 100
        };
        itemData.parentItemId = Shared.ItemList.Wooden_Sword;
        break;

    case Shared.ItemList.Divine_Sword:
        itemData.displayId = 'DivineSword';
        itemData.cost = 450;
        itemData.bonusStats = {
            damage: 12,
            maxHealth: 170,
            cooldownReduction: 0.1
        };
        itemData.parentItemId = Shared.ItemList.Iron_Sword;
        itemData.isUsable = true;
        break;

    case Shared.ItemList.Iron_Basher:
        itemData.displayId = 'IronBasher';
        itemData.cost = 550;
        itemData.bonusStats = {
            damage: 16,
            armor: 4,
            maxHealth: 100
        };
        itemData.innerCooldown = 100;
        itemData.parentItemId = Shared.ItemList.Iron_Sword;
        break;

    case Shared.ItemList.Cold_Sword:
        itemData.displayId = 'ColdSword';
        itemData.cost = 480;
        itemData.bonusStats = {
            damage: 18,
            attackSpeed: 0.30,
        };
        itemData.parentItemId = Shared.ItemList.Light_Slayer;
        break;

    case Shared.ItemList.Demon_Sabre:
        itemData.displayId = 'DemonSabre';
        itemData.cost = 500;
        itemData.bonusStats = { damage: 20 };
        itemData.parentItemId = Shared.ItemList.Katana;
        break;

        /** Wooden bow */
    case Shared.ItemList.Reckless_Longbow:
        itemData.displayId = 'RecklessLongbow';
        itemData.cost = 350;
        itemData.bonusStats = { attackSpeed: 0.30 };
        itemData.parentItemId = Shared.ItemList.Wooden_Bow;
        break;

    case Shared.ItemList.Corrupted_Longbow:
        itemData.displayId = 'CorruptedLongbow';
        itemData.cost = 500;
        itemData.bonusStats = { attackSpeed: 0.30, damage: 12 };
        itemData.parentItemId = Shared.ItemList.Poison_Bow;
        itemData.isUsable = true;
        break;

    case Shared.ItemList.Rapids_Longbow:
        itemData.displayId = 'RapidsLongbow';
        itemData.cost = 450;
        itemData.bonusStats = { attackSpeed: 0.72 };
        itemData.parentItemId = Shared.ItemList.Reckless_Longbow;
        break;

    case Shared.ItemList.Rapids_Longbow_T2:
        itemData.displayId = 'RapidsLongbow2';
        itemData.cost = 450;
        itemData.bonusStats = { attackSpeed: 1.2 };
        itemData.parentItemId = Shared.ItemList.Rapids_Longbow;
        itemData.isUsable = true;
        break;

    case Shared.ItemList.Poison_Bow:
        itemData.displayId = 'PoisonBow';
        itemData.cost = 250;
        itemData.bonusStats = { attackSpeed: 0.15, damage: 4 };
        itemData.parentItemId = Shared.ItemList.Wooden_Bow;
        break;

    case Shared.ItemList.Berserker_Bow:
        itemData.displayId = 'BerserkersBow';
        itemData.cost = 550;
        itemData.bonusStats = { attackSpeed: 0.30, maxHealth: 125, cooldownReduction: 0.1 };
        itemData.parentItemId = Shared.ItemList.Reckless_Longbow;
        break;

    case Shared.ItemList.Magical_Bow:
        itemData.displayId = 'MagicalBow';
        itemData.cost = 550;
        itemData.bonusStats = { attackSpeed: 0.35, abilityPower: 30, cooldownReduction: 0.10 };
        itemData.innerCooldown = 2000;
        itemData.parentItemId = Shared.ItemList.Poison_Bow;
        break;

        /** Buckler */
    case Shared.ItemList.Enduring_Shield:
        itemData.displayId = 'EnduringShield';
        itemData.cost = 275;
        itemData.bonusStats = { armor: 3, hpRegen: 3 };
        itemData.parentItemId = Shared.ItemList.Buckler;
        break;

    case Shared.ItemList.Vampiric_Shield:
        itemData.displayId = 'VampiricShield';
        itemData.cost = 550;
        itemData.bonusStats = { armor: 4, hpRegen: 6 };
        itemData.parentItemId = Shared.ItemList.Enduring_Shield;
        break;

    case Shared.ItemList.Iron_Buckler:
        itemData.displayId = 'IronBuckler';
        itemData.cost = 250;
        itemData.bonusStats = { armor: 4, maxHealth: 75 };
        itemData.parentItemId = Shared.ItemList.Buckler;
        break;

    case Shared.ItemList.Plate_Shield:
        itemData.displayId = 'PlateShield';
        itemData.cost = 500;
        itemData.bonusStats = { armor: 7, maxHealth: 100 };
        itemData.parentItemId = Shared.ItemList.Iron_Buckler;
        itemData.isUsable = true;
        break;

    case Shared.ItemList.Divine_Shield:
        itemData.displayId = 'DivineShield';
        itemData.cost = 525;
        itemData.bonusStats = { maxHealth: 120, armor: 4, cooldownReduction: 0.1 };
        itemData.parentItemId = Shared.ItemList.Iron_Buckler;
        itemData.isUsable = true;
        break;

    case Shared.ItemList.Magical_Shield:
        itemData.displayId = 'MagicalShield';
        itemData.cost = 300;
        itemData.bonusStats = { magicDef: 5, hpRegen: 3 };
        itemData.parentItemId = Shared.ItemList.Buckler;
        break;

    case Shared.ItemList.Kirins_Defender:
        itemData.displayId = 'KirinsDefender';
        itemData.cost = 400;
        itemData.bonusStats = { magicDef: 7.2, hpRegen: 6 };
        itemData.parentItemId = Shared.ItemList.Magical_Shield;
        break;

    case Shared.ItemList.Spike_Shield:
        itemData.displayId = 'SpikeShield';
        itemData.cost = 500;
        itemData.bonusStats = { maxHealth: 170, armor: 3 };
        itemData.parentItemId = Shared.ItemList.Iron_Buckler;
        itemData.isUsable = true;
        break;

    case Shared.ItemList.GarunsDefender:
        itemData.displayId = 'GarunsDefender';
        itemData.cost = 500;
        itemData.bonusStats = { armor: 5, hpRegen: 3 };
        itemData.parentItemId = Shared.ItemList.Enduring_Shield;
        itemData.isUsable = true;
        break;

        /** Ring */
    case Shared.ItemList.Ring_Of_Regeneration:
        itemData.displayId = 'RingofRegeneration';
        itemData.cost = 200;
        itemData.bonusStats = { hpRegen: 4 };
        itemData.parentItemId = Shared.ItemList.Iron_Ring;
        break;

    case Shared.ItemList.Gold_Ring:
        itemData.displayId = 'GoldRing';
        itemData.cost = 500;
        itemData.bonusStats = { hpRegen: 5, armor: 3 };
        itemData.parentItemId = Shared.ItemList.Ring_Of_Regeneration;
        break;

    case Shared.ItemList.Ring_Of_Time:
        itemData.displayId = 'RingofTime';
        itemData.cost = 250;
        itemData.bonusStats = { hpRegen: 3, cooldownReduction: 0.1 };
        itemData.parentItemId = Shared.ItemList.Iron_Ring;
        break;

    case Shared.ItemList.Frost_Ring:
        itemData.displayId = 'FrostRing';
        itemData.cost = 600;
        itemData.bonusStats = { abilityPower: 12, cooldownReduction: 0.12, hpRegen: 5 };
        itemData.parentItemId = Shared.ItemList.Ring_Of_Time;
        itemData.isUsable = true;
        break;

    case Shared.ItemList.Corrupted_Ring:
        itemData.displayId = 'CorruptedRing';
        itemData.cost = 500;
        itemData.bonusStats = { cooldownReduction: 0.15, maxHealth: 150, hpRegen: 6 };
        itemData.isUsable = true;
        itemData.parentItemId = Shared.ItemList.Ring_Of_Time;
        break;

    case Shared.ItemList.Berserker_Ring:
        itemData.displayId = 'BerserkerRing';
        itemData.cost = 600;
        itemData.bonusStats = { hpRegen: 6, cooldownReduction: 0.15, attackSpeed: 0.25 };
        itemData.parentItemId = Shared.ItemList.Ring_Of_Time;
        break;

    case Shared.ItemList.Chronos_Ring:
        itemData.displayId = 'ChronosRing';
        itemData.cost = 550;
        itemData.bonusStats = { abilityPower: 20, hpRegen: 4 };
        itemData.isUsable = true;
        itemData.parentItemId = Shared.ItemList.Ring_Of_Regeneration;
        break;

    case Shared.ItemList.Plague_Ring:
        itemData.displayId = 'PlagueRing';
        itemData.cost = 500;
        itemData.bonusStats = { abilityPower: 25, hpRegen: 4, cooldownReduction: 0.1 };
        itemData.parentItemId = Shared.ItemList.Ring_Of_Regeneration;
        break;

    case Shared.ItemList.Demonic_Ring:
        itemData.displayId = 'DemonicRing';
        itemData.cost = 550;
        itemData.bonusStats = { attackSpeed: 0.35, hpRegen: 5, maxHealth: 150 };
        itemData.parentItemId = Shared.ItemList.Ring_Of_Regeneration;
        break;

        /** Boots */
    case Shared.ItemList.Wizard_Shoes:
        itemData.displayId = 'WizardShoes';
        itemData.cost = 300;
        itemData.bonusStats = { moveSpeed: 12, cooldownReduction: 0.12 };
        itemData.parentItemId = Shared.ItemList.Boots;
        itemData.isBootsType = true;
        break;

    case Shared.ItemList.Agility_Boots:
        itemData.displayId = 'AgilityBoots';
        itemData.cost = 300;
        itemData.bonusStats = { moveSpeed: 12, attackSpeed: 0.25 };
        itemData.parentItemId = Shared.ItemList.Boots;
        itemData.isBootsType = true;
        break;

    case Shared.ItemList.Traveling_Boots:
        itemData.displayId = 'TravelingBoots';
        itemData.cost = 350;
        itemData.bonusStats = { moveSpeed: 18 };
        itemData.parentItemId = Shared.ItemList.Boots;
        itemData.isBootsType = true;
        break;

    case Shared.ItemList.Divine_Boots:
        itemData.displayId = 'DivineBoots';
        itemData.cost = 300;
        itemData.bonusStats = { maxHealth: 100, armor: 3, moveSpeed: 10 };
        itemData.parentItemId = Shared.ItemList.Boots;
        itemData.isBootsType = true;
        break;

        /** Nowice staff */
    case Shared.ItemList.Wizard_Staff:
        itemData.displayId = 'WizardStaff';
        itemData.cost = 300;
        itemData.bonusStats = {
            abilityPower: 26
        };
        itemData.parentItemId = Shared.ItemList.Novice_Staff;
        break;

    case Shared.ItemList.Burning_Rod:
        itemData.displayId = 'BurningRod';
        itemData.cost = 500;
        itemData.bonusStats = {
            abilityPower: 18,
            maxHealth: 110
        };
        itemData.parentItemId = Shared.ItemList.Rod_Of_Nature;
        break;

    case Shared.ItemList.Vampiric_Rod:
        itemData.displayId = 'VampiricRod';
        itemData.cost = 450;
        itemData.bonusStats = {
            abilityPower: 25,
            hpRegen: 3,
            maxHealth: 150
        };
        itemData.parentItemId = Shared.ItemList.Rod_Of_Nature;
        break;

    case Shared.ItemList.Kirin_Staff:
        itemData.displayId = 'KirinStaff';
        itemData.cost = 500;
        itemData.bonusStats = {
            abilityPower: 36,
        };
        itemData.parentItemId = Shared.ItemList.Wizard_Staff;
        break;

    case Shared.ItemList.Corrupted_Staff:
        itemData.displayId = 'CorruptedStaff';
        itemData.cost = 675;
        itemData.bonusStats = {
            abilityPower: 32,
        };
        itemData.parentItemId = Shared.ItemList.Wizard_Staff;
        break;

    case Shared.ItemList.Frozen_Staff:
        itemData.displayId = 'FrozenStaff';
        itemData.cost = 500;
        itemData.bonusStats = {
            abilityPower: 32,
            cooldownReduction: 0.08
        };
        itemData.parentItemId = Shared.ItemList.Wizard_Staff;
        break;

    case Shared.ItemList.Iron_Rod:
        itemData.displayId = 'IronRod';
        itemData.cost = 350;
        itemData.bonusStats = {
            abilityPower: 18,
            damage: 9
        };
        itemData.parentItemId = Shared.ItemList.Novice_Staff;
        break;

    case Shared.ItemList.Magic_Harpoon:
        itemData.displayId = 'MagicHarpoon';
        itemData.cost = 550;
        itemData.bonusStats = {
            abilityPower: 32,
            damage: 15
        };
        itemData.parentItemId = Shared.ItemList.Iron_Rod;
        break;

    case Shared.ItemList.Orchid_of_Malevolence:
        itemData.displayId = 'OrchidofMalevolence';
        itemData.cost = 550;
        itemData.bonusStats = {
            abilityPower: 20,
            damage: 15,
            attackSpeed: 0.35
        };
        itemData.isUsable = true;
        itemData.parentItemId = Shared.ItemList.Iron_Rod;
        break;

    case Shared.ItemList.Rod_Of_Nature:
        itemData.displayId = 'RodofNature';
        itemData.cost = 300;
        itemData.bonusStats = {
            abilityPower: 16,
            maxHealth: 100
        };
        itemData.parentItemId = Shared.ItemList.Novice_Staff;
        break;

    case Shared.ItemList.Divine_Staff_T2:
        itemData.displayId = 'DivineStaff';
        itemData.cost = 550;
        itemData.bonusStats = {
            abilityPower: 16,
            maxHealth: 120,
            cooldownReduction: 0.10,
        };
        itemData.isUsable = true;
        itemData.parentItemId = Shared.ItemList.Rod_Of_Nature;
        break;

        /** Shirt */
    case Shared.ItemList.Iron_Armor:
        itemData.displayId = 'IronArmor';
        itemData.cost = 300;
        itemData.bonusStats = { maxHealth: 150 };
        itemData.parentItemId = Shared.ItemList.Shirt;
        break;

    case Shared.ItemList.Plate_Armor:
        itemData.displayId = 'PlateArmor';
        itemData.cost = 550;
        itemData.bonusStats = { maxHealth: 200, hpRegen: 5 };
        itemData.parentItemId = Shared.ItemList.Iron_Armor;
        break;

    case Shared.ItemList.Frost_Armor:
        itemData.displayId = 'FrostArmor';
        itemData.cost = 500;
        itemData.bonusStats = { maxHealth: 135, attackSpeed: 0.25, armor: 5 };
        itemData.parentItemId = Shared.ItemList.Leather_Armor;
        break;

    case Shared.ItemList.Leather_Armor:
        itemData.displayId = 'LeatherArmor';
        itemData.cost = 250;
        itemData.bonusStats = {
            maxHealth: 90,
            attackSpeed: 0.12,
            armor: 2
        };
        itemData.parentItemId = Shared.ItemList.Shirt;
        break;

    case Shared.ItemList.Void_Armor:
        itemData.displayId = 'VoidArmor';
        itemData.cost = 500;
        itemData.bonusStats = {
            maxHealth: 135,
            attackSpeed: 0.25,
            armor: 4
        };
        itemData.parentItemId = Shared.ItemList.Leather_Armor;
        itemData.isUsable = true;
        break;

    case Shared.ItemList.Titans_Armor:
        itemData.displayId = 'TitansArmor';
        itemData.cost = 500;
        itemData.bonusStats = {
            maxHealth: 200,
            abilityPower: 15,
            armor: 4
        };
        itemData.parentItemId = Shared.ItemList.Iron_Armor;
        itemData.isUsable = true;
        break;

    case Shared.ItemList.ChestOfMalevolence:
        itemData.displayId = 'ChestofMalevolence';
        itemData.cost = 500;
        itemData.bonusStats = { 
            maxHealth: 230, 
            cooldownReduction: 0.12
        };
        itemData.parentItemId = Shared.ItemList.Iron_Armor;
        break;

    default: return;
    }
};

export default getItemStats;"""
import re
split = z.split("\n")

import json
name_to_png_name = {}

for i, line in enumerate(split):
    if "case" in line:
        name = line.split(".")[2].replace(":", "")
        match = re.search(r"itemData.displayId = '(\w+)'", split[i+1])
        if match:
            png_name = match.group(1)
            name_to_png_name[name] = png_name + ".png"

with open("item_names_to_png_names.json", "w") as f:
    json.dump(name_to_png_name, f, indent=4)