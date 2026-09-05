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
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.mytos.bio/
- group: auth
  title: ''
  type: TrustCenter
  url: security/mytos-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.mytos.bio/
- group: auth
  title: ''
  type: Security
  url: https://trust.mytos.bio/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/mytos-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mytos-domain-security.yml
created: '2026-07-17'
description: Mytos is a contract development and manufacturing organization (CDMO) for regenerative medicine and cell therapy. Its iDEM automation platform automates every unit operation of cell culture — coating, seeding, feeding, imaging, passaging and harvesting — in standard 2D T-flask formats, letting clinical-stage biotech companies transfer their manual protocols to automated GMP production at up to 50% lower batch cost, with 10x less labor and cleanroom footprint per batch. Mytos operates a CDMO facility within the Cell and Gene Therapy Catapult site and is backed by Wing Venture Capital. No public developer/API surface was found during enrichment; the profile captures the company's verified security posture (trust center, SOC 2/SOC 3/21 CFR Part 11, domain security, vulnerability disclosure).
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mytos.png
layout: provider
modified: '2026-07-20'
name: Mytos
nav: Providers
network: true
overview: Mytos is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Cell Therapy, Regenerative Medicine, and Manufacturing Automation.
random_paper: 5
score:
  band: minimal
  composite: 9.9
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 9.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 21.3
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mytos/refs/heads/main/screenshots/mytos-2026-08-07T184550.png
security:
- kind: domain-security
  name: Mytos Domain Security
  slug: mytos-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Mytos Vulnerability Disclosure
  slug: mytos-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Mytos Trust Center
  slug: mytos-trust-center
  summary_line: SOC 2 Type 2 (2025), SOC 3 (2025), 21 CFR Part 11
slug: mytos
tags:
- Company
- Biotechnology
- Cell Therapy
- Regenerative Medicine
- Manufacturing Automation
- CDMO
- Life Sciences
website: https://www.mytos.bio/
---
