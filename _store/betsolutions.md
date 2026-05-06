---
aid: betsolutions
url: https://raw.githubusercontent.com/api-evangelist/betsolutions/refs/heads/main/apis.yml
name: BetSolutions
tags:
  - Betting
  - Casinos
  - Gaming
  - Gambling
  - Slots
  - Sports Betting
x-type: company
created: '2025-02-24'
modified: '2026-04-19'
description: BetSolutions provides a casino and gaming platform API offering a two-way HTTP API with JSON data format for implementing requests and responses for slots, single and multiplayer games, and other casino platform services. The platform supports transfer and seamless wallet integration modes, slot campaigns with freespins, table games, provably fair games, poker, and third-party sportsbook integrations. Authentication uses SHA-256 hash-based signing with merchant secret keys.
apis:
  - aid: betsolutions:wallet-api
    name: BetSolutions Wallet API
    tags:
      - Wallet
      - Payments
      - Transfer
      - Seamless
    humanURL: https://docs.betsolutions.com/
    properties:
      - type: Documentation
        url: https://docs.betsolutions.com/
      - type: OpenAPI
        url: openapi/betsolutions-wallet-api.yaml
    description: Two-mode wallet integration for casino operators. Transfer mode provides deposit, withdraw, and balance operations managed by BetSolutions. Seamless mode enables operator-side wallet management with bet, win, cancel bet, change win, and balance endpoints called by BetSolutions on the operator's server.
  - aid: betsolutions:player-api
    name: BetSolutions Player API
    tags:
      - Players
      - Accounts
      - Information
    humanURL: https://docs.betsolutions.com/
    properties:
      - type: Documentation
        url: https://docs.betsolutions.com/
    description: Player information and data retrieval endpoints including player profile details, rake data by date range, and game list retrieval with product metadata.
  - aid: betsolutions:slots-api
    name: BetSolutions Slots API
    tags:
      - Slots
      - Campaigns
      - Freespins
      - Gaming
    humanURL: https://docs.betsolutions.com/
    properties:
      - type: Documentation
        url: https://docs.betsolutions.com/
    description: Slot game integration and campaign management including freespin campaign creation, deactivation, configuration retrieval, and player assignment for promotional campaigns.
  - aid: betsolutions:table-games-api
    name: BetSolutions Table Games API
    tags:
      - Table Games
      - Multiplayer
      - Tournaments
      - Gaming
    humanURL: https://docs.betsolutions.com/
    properties:
      - type: Documentation
        url: https://docs.betsolutions.com/
    description: Multiplayer table game integration supporting Backgammon, Bura, Okey, Domino, and Seka. Includes tournament management with types and statuses, and achievement systems for player engagement.
  - aid: betsolutions:provably-fair-api
    name: BetSolutions Provably Fair Games API
    tags:
      - Provably Fair
      - Zeppelin
      - Gaming
    humanURL: https://docs.betsolutions.com/
    properties:
      - type: Documentation
        url: https://docs.betsolutions.com/
    description: Provably fair game integration for Zeppelin, High Low, Dice, Mines, and Plinko. Provides jackpot history, multiplier history, and freebet creation for provably fair game mechanics.
  - aid: betsolutions:third-party-api
    name: BetSolutions Third-Party Integration API
    tags:
      - Sportsbook
      - BCBetting
      - Integration
    humanURL: https://docs.betsolutions.com/
    properties:
      - type: Documentation
        url: https://docs.betsolutions.com/
    description: Third-party sportsbook integration starting with BCBetting, providing bet retrieval, bonus management, and player-specific bonus operations.
common:
  - type: Documentation
    url: https://docs.betsolutions.com/
  - type: Authentication
    url: https://docs.betsolutions.com/
  - type: Website
    url: https://betsolutions.com
  - type: SDK
    url: https://www.nuget.org/packages/BetSolutions
    title: .NET SDK (NuGet)
  - type: SDK
    url: https://packagist.org/packages/betsolutions/casino-api
    title: PHP SDK (Composer)
  - type: Features
    data:
      - name: Transfer Wallet Mode
        description: BetSolutions-managed wallet with deposit, withdraw, and balance operations for casino operators.
      - name: Seamless Wallet Mode
        description: Operator-side wallet integration where BetSolutions calls the operator's server for bet, win, and balance operations.
      - name: SHA-256 Authentication
        description: Secure request signing using SHA-256 hash algorithm with merchant secret keys and pipe-separated parameter concatenation.
      - name: Slot Games
        description: Slot game integration with freespin campaign management, player assignment, and campaign configuration.
      - name: Table Games
        description: Multiplayer table games including Backgammon, Bura, Okey, Domino, and Seka with tournament support.
      - name: Provably Fair Games
        description: Cryptographically verifiable games including Zeppelin, High Low, Dice, Mines, and Plinko.
      - name: Poker
        description: Poker integration with jackpot tracking and daily financial reporting.
      - name: Third-Party Sportsbook
        description: Integration with BCBetting sportsbook platform for bet and bonus management.
      - name: SDK Packages
        description: Official SDK packages available for .NET (NuGet), PHP (Composer), and Java (JAR) platforms.
      - name: Multi-Language Support
        description: API supports 11 languages for international casino operator deployments.
      - name: Multi-Currency Support
        description: ISO 4217 currency codes for international payment processing.
  - type: UseCases
    data:
      - name: Casino Platform Integration
        description: Online casino operators integrate BetSolutions APIs to offer slots, table games, and card games to players.
      - name: Wallet Integration
        description: Casino operators choose transfer or seamless wallet mode to manage player funds and game transactions.
      - name: Freespin Campaigns
        description: Marketing teams create and manage freespin slot campaigns to acquire and retain players.
      - name: Tournament Management
        description: Operators run tournaments for multiplayer table games with configurable types and prize structures.
      - name: Provably Fair Gaming
        description: Platforms offering cryptographically verifiable game results using BetSolutions' provably fair API.
      - name: Sportsbook Integration
        description: Operators add sports betting capabilities through the BCBetting third-party integration.
  - type: Integrations
    data:
      - name: BCBetting
        description: Third-party sportsbook integration providing sports betting functionality for casino operators.
      - name: NuGet Package Manager
        description: .NET SDK available via NuGet for easy integration in .NET casino platform backends.
      - name: Composer Package Manager
        description: PHP SDK available via Composer for PHP-based casino platform implementations.
      - name: Java JAR
        description: Java SDK available as a JAR package for Java-based casino platform implementations.
  - type: SpectralRules
    url: rules/betsolutions-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/casino-platform.yaml
  - type: Vocabulary
    url: vocabulary/betsolutions-vocabulary.yaml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
