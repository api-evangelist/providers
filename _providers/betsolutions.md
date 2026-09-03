---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Betsolutions Agentic Access
  operation_count: 6
  slug: betsolutions-agentic-access
  summary_line: 6 operations · 5 acting
api_count: 7
apis:
- description: Player information and data retrieval endpoints including player profile details, rake data by date range, and game list retrieval with product metadata.
  name: BetSolutions Player API
  slug: player-api
- description: Slot game integration and campaign management including freespin campaign creation, deactivation, configuration retrieval, and player assignment for promotional campaigns.
  name: BetSolutions Slots API
  slug: slots-api
- description: Multiplayer table game integration supporting Backgammon, Bura, Okey, Domino, and Seka. Includes tournament management with types and statuses, and achievement systems for player engagement.
  name: BetSolutions Table Games API
  slug: table-games-api
- description: Provably fair game integration for Zeppelin, High Low, Dice, Mines, and Plinko. Provides jackpot history, multiplier history, and freebet creation for provably fair game mechanics.
  name: BetSolutions Provably Fair Games API
  slug: provably-fair-api
- description: Third-party sportsbook integration starting with BCBetting, providing bet retrieval, bonus management, and player-specific bonus operations.
  name: BetSolutions Third-Party Integration API
  slug: third-party-api
- baseURL: https://api.betsolutions.com/v1
  baseurl_source: spec
  description: Player information and game data retrieval
  name: BetSolutions Player API
  slug: betsolutions-player-api
- baseURL: https://api.betsolutions.com/v1
  baseurl_source: spec
  description: BetSolutions-managed wallet operations for transfer mode integration
  name: BetSolutions Transfer Wallet API
  slug: betsolutions-transfer-wallet-api
artifact_total: 95
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: BetSolutions Wallet Player API
  slug: open-betsolutions-player-api
- collection_type: open
  name: BetSolutions Wallet Player Transfer Wallet API
  slug: open-betsolutions-transfer-wallet-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/betsolutions-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/betsolutions-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/betsolutions-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/betsolutions-llc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/betsolutions-games
- group: docs
  title: ''
  type: Documentation
  url: https://docs.betsolutions.com/
- group: auth
  title: ''
  type: Authentication
  url: https://docs.betsolutions.com/
- group: company
  title: ''
  type: Website
  url: https://betsolutions.com
- group: build
  title: .NET SDK (NuGet)
  type: SDKs
  url: https://www.nuget.org/packages/BetSolutions
- group: build
  title: PHP SDK (Composer)
  type: SDKs
  url: https://packagist.org/packages/betsolutions/casino-api
- group: design
  title: ''
  type: SpectralRules
  url: rules/betsolutions-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/betsolutions-vocabulary.yaml
created: '2025-02-24'
description: BetSolutions provides a casino and gaming platform API offering a two-way HTTP API with JSON data format for implementing requests and responses for slots, single and multiplayer games, and other casino platform services. The platform supports transfer and seamless wallet integration modes, slot campaigns with freespins, table games, provably fair games, poker, and third-party sportsbook integrations. Authentication uses SHA-256 hash-based signing with merchant secret keys.
examples:
- key_count: 6
  name: Betsolutions Authenticateplayer Example
  slug: betsolutions-authenticateplayer-example
- key_count: 6
  name: Betsolutions Depositfunds Example
  slug: betsolutions-depositfunds-example
- key_count: 6
  name: Betsolutions Getbalance Example
  slug: betsolutions-getbalance-example
- key_count: 6
  name: Betsolutions Getgamelist Example
  slug: betsolutions-getgamelist-example
- key_count: 6
  name: Betsolutions Getplayerinfo Example
  slug: betsolutions-getplayerinfo-example
- key_count: 6
  name: Betsolutions Withdrawfunds Example
  slug: betsolutions-withdrawfunds-example
- key_count: 3
  name: Wallet Api Auth Response Example
  slug: wallet-api-auth-response-example
- key_count: 3
  name: Wallet Api Balance Request Example
  slug: wallet-api-balance-request-example
- key_count: 4
  name: Wallet Api Balance Response Example
  slug: wallet-api-balance-response-example
- key_count: 6
  name: Wallet Api Deposit Request Example
  slug: wallet-api-deposit-request-example
- key_count: 3
  name: Wallet Api Error Response Example
  slug: wallet-api-error-response-example
- key_count: 7
  name: Wallet Api Game Example
  slug: wallet-api-game-example
- key_count: 2
  name: Wallet Api Game List Request Example
  slug: wallet-api-game-list-request-example
- key_count: 2
  name: Wallet Api Game List Response Example
  slug: wallet-api-game-list-response-example
- key_count: 3
  name: Wallet Api Player Info Request Example
  slug: wallet-api-player-info-request-example
- key_count: 8
  name: Wallet Api Player Info Response Example
  slug: wallet-api-player-info-response-example
- key_count: 4
  name: Wallet Api Wallet Transaction Response Example
  slug: wallet-api-wallet-transaction-response-example
- key_count: 6
  name: Wallet Api Withdraw Request Example
  slug: wallet-api-withdraw-request-example
features:
- description: BetSolutions-managed wallet with deposit, withdraw, and balance operations for casino operators.
  name: Transfer Wallet Mode
- description: Operator-side wallet integration where BetSolutions calls the operator's server for bet, win, and balance operations.
  name: Seamless Wallet Mode
- description: Secure request signing using SHA-256 hash algorithm with merchant secret keys and pipe-separated parameter concatenation.
  name: SHA-256 Authentication
- description: Slot game integration with freespin campaign management, player assignment, and campaign configuration.
  name: Slot Games
- description: Multiplayer table games including Backgammon, Bura, Okey, Domino, and Seka with tournament support.
  name: Table Games
- description: Cryptographically verifiable games including Zeppelin, High Low, Dice, Mines, and Plinko.
  name: Provably Fair Games
- description: Poker integration with jackpot tracking and daily financial reporting.
  name: Poker
- description: Integration with BCBetting sportsbook platform for bet and bonus management.
  name: Third-Party Sportsbook
- description: Official SDK packages available for .NET (NuGet), PHP (Composer), and Java (JAR) platforms.
  name: SDK Packages
- description: API supports 11 languages for international casino operator deployments.
  name: Multi-Language Support
- description: ISO 4217 currency codes for international payment processing.
  name: Multi-Currency Support
finops:
- name: Betsolutions Finops
  service_category: iGaming Platform / Casino APIs
  slug: betsolutions-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/betsolutions.png
integrations:
- description: Third-party sportsbook integration providing sports betting functionality for casino operators.
  name: BCBetting
- description: .NET SDK available via NuGet for easy integration in .NET casino platform backends.
  name: NuGet Package Manager
- description: PHP SDK available via Composer for PHP-based casino platform implementations.
  name: Composer Package Manager
- description: Java SDK available as a JAR package for Java-based casino platform implementations.
  name: Java JAR
json_schemas:
- name: AuthResponse
  property_count: 3
  slug: betsolutions-authresponse
- name: BalanceRequest
  property_count: 3
  slug: betsolutions-balancerequest
- name: BalanceResponse
  property_count: 4
  slug: betsolutions-balanceresponse
- name: DepositRequest
  property_count: 6
  slug: betsolutions-depositrequest
- name: ErrorResponse
  property_count: 3
  slug: betsolutions-errorresponse
- name: Game
  property_count: 7
  slug: betsolutions-game
- name: GameListRequest
  property_count: 2
  slug: betsolutions-gamelistrequest
- name: GameListResponse
  property_count: 2
  slug: betsolutions-gamelistresponse
- name: PlayerInfoRequest
  property_count: 3
  slug: betsolutions-playerinforequest
- name: PlayerInfoResponse
  property_count: 8
  slug: betsolutions-playerinforesponse
- name: WalletTransactionResponse
  property_count: 4
  slug: betsolutions-wallettransactionresponse
- name: WithdrawRequest
  property_count: 6
  slug: betsolutions-withdrawrequest
- name: AuthResponse
  property_count: 3
  slug: wallet-api-auth-response
- name: BalanceRequest
  property_count: 3
  slug: wallet-api-balance-request
- name: BalanceResponse
  property_count: 4
  slug: wallet-api-balance-response
- name: DepositRequest
  property_count: 6
  slug: wallet-api-deposit-request
- name: ErrorResponse
  property_count: 3
  slug: wallet-api-error-response
- name: GameListRequest
  property_count: 2
  slug: wallet-api-game-list-request
- name: GameListResponse
  property_count: 2
  slug: wallet-api-game-list-response
- name: Game
  property_count: 7
  slug: wallet-api-game
- name: PlayerInfoRequest
  property_count: 3
  slug: wallet-api-player-info-request
- name: PlayerInfoResponse
  property_count: 8
  slug: wallet-api-player-info-response
- name: WalletTransactionResponse
  property_count: 4
  slug: wallet-api-wallet-transaction-response
- name: WithdrawRequest
  property_count: 6
  slug: wallet-api-withdraw-request
json_structures:
- name: Betsolutions Structure
  property_count: 0
  slug: betsolutions-structure
- name: Wallet Api Auth Response Structure
  property_count: 3
  slug: wallet-api-auth-response-structure
- name: Wallet Api Balance Request Structure
  property_count: 3
  slug: wallet-api-balance-request-structure
- name: Wallet Api Balance Response Structure
  property_count: 4
  slug: wallet-api-balance-response-structure
- name: Wallet Api Deposit Request Structure
  property_count: 6
  slug: wallet-api-deposit-request-structure
- name: Wallet Api Error Response Structure
  property_count: 3
  slug: wallet-api-error-response-structure
- name: Wallet Api Game List Request Structure
  property_count: 2
  slug: wallet-api-game-list-request-structure
- name: Wallet Api Game List Response Structure
  property_count: 2
  slug: wallet-api-game-list-response-structure
- name: Wallet Api Game Structure
  property_count: 7
  slug: wallet-api-game-structure
- name: Wallet Api Player Info Request Structure
  property_count: 3
  slug: wallet-api-player-info-request-structure
- name: Wallet Api Player Info Response Structure
  property_count: 8
  slug: wallet-api-player-info-response-structure
- name: Wallet Api Wallet Transaction Response Structure
  property_count: 4
  slug: wallet-api-wallet-transaction-response-structure
- name: Wallet Api Withdraw Request Structure
  property_count: 6
  slug: wallet-api-withdraw-request-structure
jsonld:
- class_count: 14
  name: Betsolutions Wallet Api Context
  property_count: 23
  slug: betsolutions-wallet-api-context
layout: provider
modified: '2026-05-19'
name: BetSolutions
nav: Providers
network: true
overview: 'BetSolutions publishes 2 APIs on the [APIs.io](https://apis.io/) network: Player API and Transfer Wallet API. Tagged areas include Betting, Casinos, Gaming, Gambling, and Slots.


  The BetSolutions catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  BetSolutions'' developer surface includes authentication, documentation, and 10 more developer resources.'
plans:
- name: Betsolutions Plans Pricing
  plan_count: 1
  slug: betsolutions-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 2
  name: Betsolutions Rate Limits
  slug: betsolutions-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: BetSolutions API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: betsolutions-jsonschema-spectral-rules
- effective_rule_count: 74
  extends:
  - spectral:oas
  name: BetSolutions API Rules
  rule_count: 33
  severity_counts:
    error: 15
    hint: 0
    info: 3
    warn: 15
  slug: betsolutions-spectral-rules
score:
  band: emerging
  composite: 24.9
  coverage:
    artifact_dirs: 15
    catalog_gap: 52.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 28.8
    contract_quality: 22.4
    developer_ergonomics: 28.6
    discoverability: 64.8
    governance: 28.8
    operational_transparency: 7.9
  previous_composite: 24.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/betsolutions/refs/heads/main/screenshots/betsolutions-2026-06-20T173201.png
security:
- kind: authentication
  name: Betsolutions Authentication
  slug: betsolutions-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Betsolutions Domain Security
  slug: betsolutions-domain-security
  summary_line: TLSv1.3 · DMARC
slug: betsolutions
tags:
- Betting
- Casinos
- Gaming
- Gambling
- Slots
- Sports Betting
use_cases:
- description: Online casino operators integrate BetSolutions APIs to offer slots, table games, and card games to players.
  name: Casino Platform Integration
- description: Casino operators choose transfer or seamless wallet mode to manage player funds and game transactions.
  name: Wallet Integration
- description: Marketing teams create and manage freespin slot campaigns to acquire and retain players.
  name: Freespin Campaigns
- description: Operators run tournaments for multiplayer table games with configurable types and prize structures.
  name: Tournament Management
- description: Platforms offering cryptographically verifiable game results using BetSolutions' provably fair API.
  name: Provably Fair Gaming
- description: Operators add sports betting capabilities through the BCBetting third-party integration.
  name: Sportsbook Integration
website: https://betsolutions.com
---
