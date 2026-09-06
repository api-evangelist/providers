---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''http://www.exacttarget.com/'', ''status'': 301, ''note'': ''declared website redirects to https://www.salesforce.com/marketing/engagement/?d=www.exacttarget.com%2F&internal=true&bc=DB — a different registrable domain (exacttarget.com -> salesforce.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/salesforce/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/exact-target-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://www.exacttarget.com/
created: '2026-07-17'
description: ExactTarget was a digital marketing and email-marketing automation SaaS company founded in 2000 in Indianapolis, Indiana. It built the Fuel developer platform and Interactive Marketing Hub for email, mobile, and social campaign automation, went public on the NYSE (ticker ET) in March 2012, and was acquired by Salesforce in December 2013 for approximately 2.5 billion dollars. ExactTarget became the foundation of Salesforce Marketing Cloud; the exacttarget.com domain now redirects to the Salesforce Marketing Cloud email-marketing product and the former developer.exacttarget.com Fuel/Code@ API platform (REST and SOAP APIs) has been retired and folded into the Salesforce Marketing Cloud developer surface. This profile is retained in the API Evangelist network as a historical/acquired-company record.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/exact-target.png
layout: provider
modified: '2026-08-21'
name: Exact Target
nav: Providers
network: true
overview: Exact Target is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Email Marketing, Marketing Automation, Digital Marketing, and Software-as-a-Service.
random_paper: 7
score:
  band: minimal
  composite: 5.0
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
    operational_transparency: 0.0
  previous_composite: 5.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/exact-target/refs/heads/main/screenshots/exact-target-2026-07-25T213835.png
security:
- kind: domain-security
  name: Exact Target Domain Security
  slug: exact-target-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: exact-target
tags:
- Company
- Email Marketing
- Marketing Automation
- Digital Marketing
- Software-as-a-Service
- Acquired
- Salesforce Marketing Cloud
website: http://www.exacttarget.com/
---
