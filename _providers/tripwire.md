---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://www.tripwire.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Tripwire
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tripwire-domain-security.yml
created: '2026-07-17'
description: Tripwire Inc. (part of Fortra), headquartered in Portland, Oregon, is an enterprise cybersecurity company known for file integrity monitoring (FIM), security configuration management (SCM), and vulnerability management. Its product line includes Tripwire Enterprise, the Tripwire Axon Agent, Tripwire IP360, Tripwire ExpertOps, and the original Open Source Tripwire. Tripwire's capabilities are delivered as on-premises and managed products with product-embedded REST APIs and configuration-management integrations (Puppet, Chef, Ansible) rather than a public developer portal; there is no public developer portal, public OpenAPI, or first-party client SDK on the public package registries as of this enrichment pass. This profile was surfaced as a portfolio company of bessemer-venture-partners and is being enriched by the API Evangelist pipeline.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tripwire.png
layout: provider
modified: '2026-07-21'
name: Tripwire
nav: Providers
network: true
overview: Tripwire is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cybersecurity, File Integrity Monitoring, Security Configuration Management, and Vulnerability Management.
random_paper: 4
score:
  band: minimal
  composite: 5.3
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 5.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tripwire/refs/heads/main/screenshots/tripwire-2026-09-02T164254.png
security:
- kind: domain-security
  name: Tripwire Domain Security
  slug: tripwire-domain-security
  summary_line: TLSv1.3 · DMARC
slug: tripwire
tags:
- Company
- Cybersecurity
- File Integrity Monitoring
- Security Configuration Management
- Vulnerability Management
- Compliance
- Security
website: https://www.tripwire.com/
---
