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
artifact_total: 2
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/mckesson-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mckesson-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mckesson
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mckesson
- group: company
  title: ''
  type: Website
  url: https://www.mckesson.com
created: '2026-03-21'
description: McKesson is a Fortune 500 healthcare company providing wholesale medical supplies and equipment, pharmaceutical distribution, and healthcare technology solutions. No public developer APIs are currently documented.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mckesson.png
layout: provider
modified: '2026-04-28'
name: McKesson
nav: Providers
network: true
overview: McKesson is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Distribution, Fortune 500, Healthcare, Medical Supplies, and Pharmaceuticals.
press:
- date: '2026-05-25'
  title: Artificial Intelligence at McKesson - Three Use Cases
  url: https://emerj.com/artificial-intelligence-at-mckesson-three-use-cases/
- date: '2026-05-25'
  title: AI in Community Oncology
  url: https://www.mckesson.com/stories-insights/ai-in-community-oncology/
- date: '2026-05-25'
  title: Technology Solutions for Specialty Practices
  url: https://www.mckesson.com/specialty/technology-solutions-specialty-practices/
- date: '2026-05-25'
  title: Reducing Administrative Burden with AI Tools
  url: https://www.mckesson.com/stories-insights/reducing-administrative-burden-with-ai-tools/
- date: '2026-05-25'
  title: McKesson ties AI, automation, specialty tech to Q3 sales ...
  url: https://www.digitalcommerce360.com/2026/02/05/mckesson-ai-automation-specialty-tech-q3-sales/
random_paper: 6
score:
  band: minimal
  composite: 4.8
  coverage:
    artifact_dirs: 5
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
  previous_composite: 4.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 15.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mckesson/refs/heads/main/screenshots/mckesson-2026-06-20T185100.png
security:
- kind: domain-security
  name: Mckesson Domain Security
  slug: mckesson-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Mckesson Vulnerability Disclosure
  slug: mckesson-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
slug: mckesson
tags:
- Distribution
- Fortune 500
- Healthcare
- Medical Supplies
- Pharmaceuticals
website: https://www.mckesson.com
---
