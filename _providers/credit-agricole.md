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
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/credit-agricole/refs/heads/main/llms/credit-agricole-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/credit-agricole-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/credit-agricole/refs/heads/main/hosts/credit-agricole-hosts.yml
  title: ''
  type: Hosts
  url: hosts/credit-agricole-hosts.yml
- group: docs
  title: ''
  type: Documentation
  url: https://developer.credit-agricole.fr/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/credit-agricole/refs/heads/main/security/credit-agricole-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/credit-agricole-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.credit-agricole.fr
coverage:
  checked: '2026-10-14'
  detail: Developer portal pages load via JavaScript and no machine‑readable OpenAPI spec was found.
  evidence:
  - status: 200
    url: https://developer.credit-agricole.fr/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-14'
description: Credit Agricole is a leading French banking group offering a wide range of retail, corporate and investment banking services. It serves millions of customers through an extensive network of branches and digital channels, providing accounts, loans, payments, insurance and wealth management solutions. The group emphasizes innovation and digital transformation, supporting developers with online services and APIs across its financial ecosystem.
image: https://www.credit-agricole.fr/content/dam/assetsca/master/public/commun/images/autre/images/NPC-logo_Agir_chaque_jour_CA_H_Desktop-1.svg
layout: provider
modified: '2026-10-14'
name: Credit Agricole
nav: Providers
network: true
overview: 'Credit Agricole is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Banking, Finance, France, and Retail.


  Credit Agricole''s developer surface includes documentation and 4 more developer resources.'
random_paper: 0
score:
  band: minimal
  composite: 5.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 55.4
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 4.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Credit Agricole Domain Security
  slug: credit-agricole-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: credit-agricole
tags:
- Company
- Banking
- Finance
- France
- Retail
website: https://www.credit-agricole.fr
---
