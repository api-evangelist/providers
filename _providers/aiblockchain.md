---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-09-24'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://ai-blockchain.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aiblockchain/refs/heads/main/security/aiblockchain-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aiblockchain-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aiblockchain/refs/heads/main/llms/aiblockchain-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aiblockchain-llms.txt
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/aiblockchain/refs/heads/main/plans/aiblockchain-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aiblockchain-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/aiblockchain/refs/heads/main/rate-limits/aiblockchain-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/aiblockchain-rate-limits.yml
coverage:
  checked: '2026-09-14'
  detail: Ai-Blockchain sells enterprise blockchain and AI consulting engagements through a contact form and ships no developer surface at all — ai-blockchain.com is a purchased React marketing template deployed without SPA rewrites, so even its own /services and /contact-us routes return a hard 404 to a direct fetch; every named /.well-known/, /openapi.json, /swagger.json, /apis.json and /llms.txt path 404s on both ai-blockchain.com and www; and the one deliberately configured developer-shaped host, docs.ai-blockchain.com, is a dangling CNAME to ghs.google.com that answers a Google 404 with no TLS certificate at all.
  evidence:
  - status: 200
    url: https://ai-blockchain.com/
  - status: 404
    url: https://ai-blockchain.com/openapi.json
  - status: 404
    url: https://ai-blockchain.com/.well-known/agent-card.json
  - status: 404
    url: https://ai-blockchain.com/llms.txt
  - status: 404
    url: https://ai-blockchain.com/services
  - status: 404
    url: http://docs.ai-blockchain.com/
  reason: no-developer-program
  state: none
created: '2026-09-14'
description: 'Ai-Blockchain (also styled AI BlockChain, AIBC) is a Hoboken, New Jersey enterprise blockchain and artificial-intelligence software company founded in 2014 by Drew Hingorani and Stephen Reed. It builds a proprietary, patented private distributed ledger — US Patent 10,579,974, "Systems, methods, and program products for a distributed digital asset network with rapid transaction settlements" — that the company describes as gas-free, energy efficient and immutable, with artificial-intelligence agents managing the chain itself. Its marketed service lines are private blockchain with instant settlement, smart payment and transaction platforms, secure streaming and content distribution / digital rights management, AI-powered virtual assistants and customer-service chatbots, cloud cost optimization, a LIMS healthcare product, and custom AI + blockchain application development. It sells enterprise engagements and consulting rather than a self-serve developer product: as of September
  2026 the company publishes no developer portal, API reference, SDK, or machine-readable API contract on any host it controls.'
image: https://ai-blockchain.com/assets/img/logo-dark.webp
layout: provider
modified: '2026-09-14'
name: Ai-Blockchain
nav: Providers
network: true
overview: Ai-Blockchain is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Blockchain, Distributed Ledger, Artificial Intelligence, and Enterprise Software.
plans:
- name: Aiblockchain Plans Pricing
  plan_count: 0
  slug: aiblockchain-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Aiblockchain Rate Limits
  slug: aiblockchain-rate-limits
score:
  band: minimal
  composite: 1.5
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    operational_transparency: 0.0
  previous_composite: 1.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 9.4
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aiblockchain Domain Security
  slug: aiblockchain-domain-security
  summary_line: TLSv1.3
slug: aiblockchain
tags:
- Company
- Blockchain
- Distributed Ledger
- Artificial Intelligence
- Enterprise Software
- Digital Rights Management
- Payments
- Consulting
website: https://ai-blockchain.com/
---
