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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vaulted-deep-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://vaulteddeep.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://vaulteddeep.com/privacy-cookie-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/vaulted-deep
- group: company
  title: ''
  type: Twitter
  url: https://x.com/VaultedDeep
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/vaulted-deep-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/vaulted-deep-plans-pricing.yml
coverage:
  checked: '2026-09-02'
  detail: Vaulted Deep operates deep-well organic-waste injection sites, and its whole public surface is a three-page WordPress marketing site whose only machine-readable endpoint is the default wp-json CMS index - the AI-accelerated Site Development Platform it markets is internal tooling for developing its own wells, not a product with an API, and no api., docs. or developers. subdomain resolves in DNS.
  evidence:
  - status: 404
    url: https://vaulteddeep.com/openapi.json
  - status: 404
    url: https://vaulteddeep.com/llms.txt
  - status: 404
    url: https://vaulteddeep.com/.well-known/agent-card.json
  - status: 200
    url: https://vaulteddeep.com/wp-json/
  - status: 404
    url: https://api.github.com/orgs/vaulted-deep
  reason: not-a-software-company
  state: none
created: '2026-09-02'
description: Vaulted Deep is a permanent carbon removal and organic waste disposal company that injects carbon-filled organic waste — biosolids, agricultural byproducts and manure, and pulp and paper sludge — thousands of feet underground as a slurry, using patented geologic slurry sequestration technology adapted from oil and gas practice so the carbon is trapped permanently beneath impermeable rock. Spun out of Advantek Waste Management Services in 2023 and co-founded by Julia Reichelstein and Omar Abou-Sayed, it operates the Great Plains site in Hutchinson, Kansas and the Terminal Island site in Los Angeles, California, serving municipal wastewater utilities and agricultural operators while selling durable carbon removal credits to corporate buyers. It publishes no public API, SDK, or developer program.
image: https://vaulteddeep.com/wp-content/uploads/2026/08/Social-share.jpg
layout: provider
modified: '2026-09-02'
name: Vaulted Deep
nav: Providers
network: true
overview: Vaulted Deep is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Carbon Removal, Carbon Dioxide Removal, Climate, and Waste Management.
plans:
- name: Vaulted Deep Plans Pricing
  plan_count: 0
  slug: vaulted-deep-plans-pricing
random_paper: 19
score:
  band: minimal
  composite: 7.8
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.7
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: domain-security
  name: Vaulted Deep Domain Security
  slug: vaulted-deep-domain-security
  summary_line: TLSv1.3 · DMARC
slug: vaulted-deep
tags:
- Company
- Carbon Removal
- Carbon Dioxide Removal
- Climate
- Waste Management
- Biosolids
- Geologic Sequestration
- Sustainability
- Environment
website: https://vaulteddeep.com/
---
