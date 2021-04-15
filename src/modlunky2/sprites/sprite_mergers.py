from .full_sheets import *


def get_all_sprite_mergers(entities_json: dict, textures_json: dict, base_path: str):
    return [
        CharacterBlackSpriteMerger(base_path),
        CharacterLimeSpriteMerger(base_path),
        CharacterMagentaSpriteMerger(base_path),
        CharacterOliveSpriteMerger(base_path),
        CharacterOrangeSpriteMerger(base_path),
        CharacterPinkSpriteMerger(base_path),
        CharacterRedSpriteMerger(base_path),
        CharacterVioletSpriteMerger(base_path),
        CharacterWhiteSpriteMerger(base_path),
        CharacterYellowSpriteMerger(base_path),
        CharacterBlueSpriteMerger(base_path),
        CharacterCeruleanSpriteMerger(base_path),
        CharacterCinnabarSpriteMerger(base_path),
        CharacterCyanSpriteMerger(base_path),
        CharacterGoldSpriteMerger(base_path),
        CharacterGraySpriteMerger(base_path),
        CharacterGreenSpriteMerger(base_path),
        CharacterIrisSpriteMerger(base_path),
        CharacterKhakiSpriteMerger(base_path),
        CharacterLemonSpriteMerger(base_path),
        CharacterEggChildSpriteMerger(base_path),
        CharacterHiredHandSpriteMerger(base_path),
        TurkeySpriteMerger(entities_json, textures_json, base_path),
        RockdogSpriteMerger(entities_json, textures_json, base_path),
        AxolotlSpriteMerger(entities_json, textures_json, base_path),
        QilinSpriteMerger(entities_json, textures_json, base_path),
        MontySpriteMerger(entities_json, textures_json, base_path),
        PercySpriteMerger(entities_json, textures_json, base_path),
        PoochiSpriteMerger(entities_json, textures_json, base_path),
        SnakeSpriteMerger(entities_json, textures_json, base_path),
        BatSpriteMerger(entities_json, textures_json, base_path),
        FlySpriteMerger(entities_json, textures_json, base_path),
        SkeletonSpriteMerger(entities_json, textures_json, base_path),
        SpiderSpriteMerger(entities_json, textures_json, base_path),
        # EarSpriteMerger(entities_json, textures_json, base_path),  # RIP Ear
        ShopkeeperSpriteMerger(entities_json, textures_json, base_path),
        UfoSpriteMerger(entities_json, textures_json, base_path),
        AlienSpriteMerger(entities_json, textures_json, base_path),
        CobraSpriteMerger(entities_json, textures_json, base_path),
        ScorpionSpriteMerger(entities_json, textures_json, base_path),
        GoldenMonkeySpriteMerger(entities_json, textures_json, base_path),
        BeeSpriteMerger(entities_json, textures_json, base_path),
        MagmarSpriteMerger(entities_json, textures_json, base_path),
        VampireSpriteMerger(entities_json, textures_json, base_path),
        VladSpriteMerger(entities_json, textures_json, base_path),
        LeprechaunSpriteMerger(entities_json, textures_json, base_path),
        CaveManSpriteMerger(entities_json, textures_json, base_path),
        BodyguardSpriteMerger(entities_json, textures_json, base_path),
        OldHunterSpriteMerger(entities_json, textures_json, base_path),
        MerchantSpriteMerger(entities_json, textures_json, base_path),
        HundunsServantSpriteMerger(entities_json, textures_json, base_path),
        ThiefSpriteMerger(entities_json, textures_json, base_path),
        ParmesanSpriteMerger(entities_json, textures_json, base_path),
        ParsleySpriteMerger(entities_json, textures_json, base_path),
        ParsnipSpriteMerger(entities_json, textures_json, base_path),
        YangSpriteMerger(entities_json, textures_json, base_path),
        BirdiesSpriteMerger(entities_json, textures_json, base_path),
        RobotSpriteMerger(entities_json, textures_json, base_path),
        ImpSpriteMerger(entities_json, textures_json, base_path),
        TikiManSpriteMerger(entities_json, textures_json, base_path),
        ManTrapSpriteMerger(entities_json, textures_json, base_path),
        CritterSnailSpriteMerger(entities_json, textures_json, base_path),
        CritterDungBeetleSpriteMerger(entities_json, textures_json, base_path),
        FireBugSpriteMerger(entities_json, textures_json, base_path),
        MoleSpriteMerger(entities_json, textures_json, base_path),
        WitchDoctorSpriteMerger(entities_json, textures_json, base_path),
        CritterButterflySpriteMerger(entities_json, textures_json, base_path),
        HornedLizardSpriteMerger(entities_json, textures_json, base_path),
        WitchDoctorSkullSpriteMerger(entities_json, textures_json, base_path),
        MonkeySpriteMerger(entities_json, textures_json, base_path),
        HangSpiderSpriteMerger(entities_json, textures_json, base_path),
        MosquitoSpriteMerger(entities_json, textures_json, base_path),
        JiangshiSpriteMerger(entities_json, textures_json, base_path),
        HermitCrabSpriteMerger(entities_json, textures_json, base_path),
        FlyingFishSpriteMerger(entities_json, textures_json, base_path),
        OctopusSpriteMerger(entities_json, textures_json, base_path),
        CritterCrabSpriteMerger(entities_json, textures_json, base_path),
        CritterBlueCrabSpriteMerger(base_path),
        FemaleJiangshiSpriteMerger(entities_json, textures_json, base_path),
        CritterFishSpriteMerger(entities_json, textures_json, base_path),
        CrocManSpriteMerger(entities_json, textures_json, base_path),
        SorceressSpriteMerger(entities_json, textures_json, base_path),
        CatMummySpriteMerger(entities_json, textures_json, base_path),
        CritterAnchovySpriteMerger(entities_json, textures_json, base_path),
        NecromancerSpriteMerger(entities_json, textures_json, base_path),
        CrittersLocustSpriteMerger(entities_json, textures_json, base_path),
        YetiSpriteMerger(entities_json, textures_json, base_path),
        ProtoShopkeeperSpriteMerger(entities_json, textures_json, base_path),
        CritterFireflySpriteMerger(entities_json, textures_json, base_path),
        PenguinSpriteMerger(entities_json, textures_json, base_path),
        DroneSpriteMerger(entities_json, textures_json, base_path),
        SlimeSpriteMerger(entities_json, textures_json, base_path),
        JumpdogSpriteMerger(entities_json, textures_json, base_path),
        TadpoleSpriteMerger(entities_json, textures_json, base_path),
        OlmiteNakedSpriteMerger(entities_json, textures_json, base_path),
        OlmitedArmoredSpriteMerger(base_path),
        OlmiteHelmetSpriteMerger(base_path),
        GrubSpriteMerger(entities_json, textures_json, base_path),
        FrogSpriteMerger(entities_json, textures_json, base_path),
        FireFrogSpriteMerger(entities_json, textures_json, base_path),
        QuillbackSpriteMerger(entities_json, textures_json, base_path),
        GiantSpiderSpriteMerger(entities_json, textures_json, base_path),
        QueenBeeSpriteMerger(entities_json, textures_json, base_path),
        MummySpriteMerger(entities_json, textures_json, base_path),
        # AnubisSpriteMerger(entities_json, textures_json, base_path),  # RIP
        # Anubis2SpriteMerger(entities_json, textures_json, base_path),  # RIP
        LamassuSpriteMerger(entities_json, textures_json, base_path),
        YetiKingSpriteMerger(entities_json, textures_json, base_path),
        YetiQueenSpriteMerger(entities_json, textures_json, base_path),
        CrabManSpriteMerger(entities_json, textures_json, base_path),
        LavamanderSpriteMerger(entities_json, textures_json, base_path),
        GiantFlySpriteMerger(entities_json, textures_json, base_path),
        GiantClamSpriteMerger(entities_json, textures_json, base_path),
        AmmitSpriteMerger(entities_json, textures_json, base_path),
        MadameTuskSpriteMerger(entities_json, textures_json, base_path),
        EggplantMinisterSpriteMerger(entities_json, textures_json, base_path),
        GiantFrogSpriteMerger(entities_json, textures_json, base_path),
        GiantFishSpriteMerger(entities_json, textures_json, base_path),
        # KinguSpriteMerger(entities_json, textures_json, base_path),  # RIP
        StorageGuySpriteMerger(entities_json, textures_json, base_path),
        OsirisSpriteMerger(entities_json, textures_json, base_path),
        AlienQueenSpriteMerger(entities_json, textures_json, base_path),
        # OlmecSpriteMerger(entities_json, textures_json, base_path),  # RIP
        # MechSpriteMerger(entities_json, textures_json, base_path),  # RIP
        GhistSpriteMerger(entities_json, textures_json, base_path),
        GhostSpriteMerger(entities_json, textures_json, base_path),
        GhostMediumSadSpriteMerger(entities_json, textures_json, base_path),
        GhostMediumHappySpriteMerger(entities_json, textures_json, base_path),
        GhostSmallSadSpriteMerger(entities_json, textures_json, base_path),
        GhostSmallHappySpriteMerger(entities_json, textures_json, base_path),
        GhostSmallSurprisedSpriteMerger(entities_json, textures_json, base_path),
        GhostSmallAngrySpriteMerger(entities_json, textures_json, base_path),
        # MegaJellySpriteMerger(entities_json, textures_json, base_path),  # RIP
    ]
