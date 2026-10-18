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
api_count: 1
apis:
- description: Certis Oncology provides a developer portal at https://www.certisoncology.com/ but no public machine‑readable API specification was found.
  name: Certis Oncology API
  slug: certis-oncology-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/certis-oncology/refs/heads/main/hosts/certis-oncology-hosts.yml
  title: ''
  type: Hosts
  url: hosts/certis-oncology-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.certisoncology.com/about-us/news/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/certis-oncology/refs/heads/main/security/certis-oncology-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/certis-oncology-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.certisoncology.com/
- group: company
  title: ''
  type: Blog
  url: https://blog.certisoncology.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.certisoncology.com/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://www.certisoncology.com/contact-us/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.certisoncology.com/about-us/our-story/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.certisoncology.com/resources/cancer-market-facts/
coverage:
  checked: '2026-10-08'
  detail: The provider's documentation at https://www.certisoncology.com/ does not expose any OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL specifications despite being publicly accessible.
  evidence:
  - status: 403
    url: https://www.certisoncology.com/openapi.json
  - status: 0
    url: https://api.certisoncology.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-07'
description: Certis Oncology is a life‑science technology company that provides pre‑clinical oncology services and AI‑enabled translational science platforms. Their Oncology Intelligence® platform integrates predictive AI with multi‑modal datasets to generate hypotheses and insights for precision oncology, offering services such as PDX models, predictive drug discovery, and comprehensive data analytics for drug developers.
image: https://www.certisoncology.com/wp-content/uploads/BarneyOI_rare-detailed-profile-1.gif
layout: provider
modified: '2026-10-07'
name: Certis Oncology
nav: Providers
network: true
overview: 'Certis Oncology is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Oncology, Artificial Intelligence, Precision-Medicine, and Preclinical.


  Certis Oncology''s developer surface includes engineering blog, support, getting-started guide, pricing, and 5 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 13.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 58.9
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Certis Oncology Domain Security
  slug: certis-oncology-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: certis-oncology
tags:
- Company
- Oncology
- Artificial Intelligence
- Precision-Medicine
- Preclinical
website: https://www.certisoncology.com/
---
