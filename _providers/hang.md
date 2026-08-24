---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.4
  scored_at: '2026-08-24'
api_count: 18
apis:
- description: The Activities API from Hang — 2 operation(s) for activities.
  name: Hang Activities API
  slug: hang-activities-api
- description: The Loot Box Reward Choices API from Hang — 2 operation(s) for loot box reward choices.
  name: Hang Loot Box Reward Choices API
  slug: hang-loot-box-reward-choices-api
- description: The Loot box reward probabilities API from Hang — 2 operation(s) for loot box reward probabilities.
  name: Hang Loot box reward probabilities API
  slug: hang-loot-box-reward-probabilities-api
- description: The Loot Boxes API from Hang — 4 operation(s) for loot boxes.
  name: Hang Loot Boxes API
  slug: hang-loot-boxes-api
- description: The Member Actions API from Hang — 3 operation(s) for member actions.
  name: Hang Member Actions API
  slug: hang-member-actions-api
- description: The Memberships API from Hang — 10 operation(s) for memberships.
  name: Hang Memberships API
  slug: hang-memberships-api
- description: The Program memberships API from Hang — 3 operation(s) for program memberships.
  name: Hang Program memberships API
  slug: hang-program-memberships-api
- description: The Program Tiers API from Hang — 1 operation(s) for program tiers.
  name: Hang Program Tiers API
  slug: hang-program-tiers-api
- description: The ProgramMembershipPuzzles API from Hang — 3 operation(s) for programmembershippuzzles.
  name: Hang ProgramMembershipPuzzles API
  slug: hang-programmembershippuzzles-api
- description: The Programs API from Hang — 2 operation(s) for programs.
  name: Hang Programs API
  slug: hang-programs-api
- description: The Puzzles API from Hang — 4 operation(s) for puzzles.
  name: Hang Puzzles API
  slug: hang-puzzles-api
- description: The Quests API from Hang — 9 operation(s) for quests.
  name: Hang Quests API
  slug: hang-quests-api
- description: The Redemptions API from Hang — 4 operation(s) for redemptions.
  name: Hang Redemptions API
  slug: hang-redemptions-api
- description: The Rewards API from Hang — 5 operation(s) for rewards.
  name: Hang Rewards API
  slug: hang-rewards-api
- description: The TokenizedRewards API from Hang — 2 operation(s) for tokenizedrewards.
  name: Hang TokenizedRewards API
  slug: hang-tokenizedrewards-api
- description: The Tokens API from Hang — 7 operation(s) for tokens.
  name: Hang Tokens API
  slug: hang-tokens-api
- description: The Users API from Hang — 1 operation(s) for users.
  name: Hang Users API
  slug: hang-users-api
- description: The Wallet Integration API from Hang — 2 operation(s) for wallet integration.
  name: Hang Wallet Integration API
  slug: hang-wallet-integration-api
artifact_total: 43
asyncapis:
- description: ''
  name: Hang Webhooks
  slug: hang-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Hang Partner API (params in:formData) Activities API
  slug: open-hang-activities-api
- collection_type: open
  name: Hang Partner API (params in:formData) Activities Loot Box Reward Choices API
  slug: open-hang-loot-box-reward-choices-api
- collection_type: open
  name: Hang Partner API (params in:formData) Activities Loot box reward probabilities API
  slug: open-hang-loot-box-reward-probabilities-api
- collection_type: open
  name: Hang Partner API (params in:formData) Activities Loot Boxes API
  slug: open-hang-loot-boxes-api
- collection_type: open
  name: Hang Partner API (params in:formData) Activities Member Actions API
  slug: open-hang-member-actions-api
- collection_type: open
  name: Hang Partner API (params in:formData) Activities Memberships API
  slug: open-hang-memberships-api
- collection_type: open
  name: Hang Partner API (params in:formData) Activities Program memberships API
  slug: open-hang-program-memberships-api
- collection_type: open
  name: Hang Partner API (params in:formData) Activities Program Tiers API
  slug: open-hang-program-tiers-api
- collection_type: open
  name: Hang Partner API (params in:formData) Activities ProgramMembershipPuzzles API
  slug: open-hang-programmembershippuzzles-api
- collection_type: open
  name: Hang Partner API (params in:formData) Activities Programs API
  slug: open-hang-programs-api
- collection_type: open
  name: Hang Partner API (params in:formData) Activities Puzzles API
  slug: open-hang-puzzles-api
- collection_type: open
  name: Hang Partner API (params in:formData) Activities Quests API
  slug: open-hang-quests-api
- collection_type: open
  name: Hang Partner API (params in:formData) Activities Redemptions API
  slug: open-hang-redemptions-api
- collection_type: open
  name: Hang Partner API (params in:formData) Activities Rewards API
  slug: open-hang-rewards-api
- collection_type: open
  name: Hang Partner API (params in:formData) Activities TokenizedRewards API
  slug: open-hang-tokenizedrewards-api
- collection_type: open
  name: Hang Partner API (params in:formData) Activities Tokens API
  slug: open-hang-tokens-api
- collection_type: open
  name: Hang Partner API (params in:formData) Activities Users API
  slug: open-hang-users-api
- collection_type: open
  name: Hang Partner API (params in:formData) Activities Wallet Integration API
  slug: open-hang-wallet-integration-api
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/hang-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/hang-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hang-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hang-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.hang.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.hang.com/hang-platform
- group: docs
  title: ''
  type: Documentation
  url: https://docs.hang.com/hang-platform
- group: docs
  title: ''
  type: APIReference
  url: https://app.swaggerhub.com/apis/Hang.xyz/hang_partner_api/2023.09.07
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.hang.com/hang-platform/api-usage/creating-program-memberships-for-new-users
- group: operate
  title: ''
  type: StatusPage
  url: https://status.hang.com
- group: start
  title: ''
  type: SignUp
  url: https://copilot.hang.com/login
- group: start
  title: ''
  type: Login
  url: https://copilot.hang.com/login
- group: commercial
  title: ''
  type: Pricing
  url: https://www.hang.com/#pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.hang.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hang.com/privacy
- group: auth
  title: ''
  type: Security
  url: https://www.hang.com/security
- group: auth
  title: ''
  type: Compliance
  url: https://www.hang.com/security
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hang-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/hang-mcp.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/hang-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/hang-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/hang-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/hang-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/hang-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/hang-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/hang-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/hang-partner-api-overlay.yaml
created: '2026-07-17'
description: Hang is a customer loyalty and engagement platform (originally a Paradigm-backed Web3 brand-loyalty company, now positioned as an AI-driven "autonomous marketing system") used by restaurant, beauty, apparel, and e-commerce brands to build and run tier-based membership and rewards programs. Its Partner API powers program memberships, points and activities, quests, challenges, puzzles, loot/mystery boxes, rewards and redemptions, balance/gift cards, tokenized rewards, program tiers and segments, plus point-of-sale integrations with Toast and Square and real-time webhooks. Brands can embed a white-labeled rewards portal or drive the whole loyalty experience programmatically through the REST API.
image: https://hang.com/og-image.png
layout: provider
mcp_servers:
- description: ''
  name: Hang MCP Server
  slug: hang-mcp-server
modified: '2026-07-19'
name: Hang
nav: Providers
network: true
overview: 'Hang publishes 18 APIs on the [APIs.io](https://apis.io/) network, including Activities API, Loot Box Reward Choices API, Loot box reward probabilities API, and 15 more. Tagged areas include Company, Consumer, Loyalty, Rewards, and Membership.


  The Hang catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Hang''s developer surface includes authentication, documentation, API reference, getting-started guide, signup flow, pricing, and 22 more developer resources.'
random_paper: 15
score:
  band: developing
  composite: 50.5
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 30.3
    contract_quality: 50.2
    developer_ergonomics: 48.2
    discoverability: 81.5
    governance: 30.3
    operational_transparency: 34.2
  previous_composite: 50.5
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 18
    mcp: derived
    skills: derived
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hang/refs/heads/main/screenshots/hang-2026-07-25T220618.png
security:
- kind: authentication
  name: Hang Authentication
  slug: hang-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Hang Domain Security
  slug: hang-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Hang Vulnerability Disclosure
  slug: hang-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Hang Trust Center
  slug: hang-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: hang
tags:
- Company
- Consumer
- Loyalty
- Rewards
- Membership
- Customer Engagement
- Marketing
- Restaurant
- Point-of-Sale
- Webhook
website: https://www.hang.com
---
