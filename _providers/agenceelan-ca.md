---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/agenceelan-ca/llms/agenceelan-ca-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agenceelan-ca-llms.txt
- group: other
  href: https://artifacts.apis.io/agenceelan-ca/hosts/agenceelan-ca-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agenceelan-ca-hosts.yml
- group: other
  href: https://artifacts.apis.io/agenceelan-ca/vendors/agenceelan-ca-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agenceelan-ca-vendors.yml
- group: company
  title: ''
  type: Blog
  url: https://www.agenceelan.ca/blog
- group: auth
  href: https://artifacts.apis.io/agenceelan-ca/security/agenceelan-ca-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agenceelan-ca-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agenceelan.ca/
coverage:
  checked: '2026-11-01'
  detail: The company provides custom AI development services and does not expose a public API.
  evidence:
  - status: 200
    url: https://www.agenceelan.ca/
  reason: not-a-software-company
  state: none
created: '2026-10-31'
description: Élan is a custom AI development studio based in Québec, offering tailored AI systems for professional service firms. Their solutions automate document handling, contract prefilling, voice submission PDFs, 3D configurators, and content generation, aiming to reduce manual effort and improve efficiency across sectors such as plumbing, mortgage, and manufacturing. The studio emphasizes Quebec‑hosted SaaS and integrates tools like Zoho, DocuSign, and LeadConnector.
image: https://www.agenceelan.ca/og-home.png
layout: provider
modified: '2026-10-31'
name: Élan
nav: Providers
network: true
overview: 'Élan is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Custom Software, Quebec, Software-as-a-Service, and Automation.


  Élan''s developer surface includes engineering blog and 5 more developer resources.'
random_paper: 20
score:
  band: minimal
  composite: 3.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.3
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 48.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - canada
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 3.9
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Agenceelan Ca Domain Security
  slug: agenceelan-ca-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: agenceelan-ca
tags:
- Artificial Intelligence
- Custom Software
- Quebec
- Software-as-a-Service
- Automation
- Company
website: https://agenceelan.ca/
---
