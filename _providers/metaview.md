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
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 3
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/metaview/refs/heads/main/plans/metaview-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/metaview-plans-pricing.yml
- group: company
  title: ''
  type: Blog
  url: https://www.metaview.ai/resources/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://content.metaview.ai/rss/
- group: company
  title: ''
  type: Website
  url: https://www.metaview.ai
- group: commercial
  title: ''
  type: Pricing
  url: https://www.metaview.ai/pricing
- group: start
  title: ''
  type: Login
  url: https://app.metaview.ai
- group: company
  title: ''
  type: Blog
  url: https://www.metaview.ai/resources
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.metaview.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.metaview.ai/privacy-policy
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/metaview/refs/heads/main/security/metaview-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/metaview-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.metaview.ai
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/metaview/refs/heads/main/llms/metaview-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/metaview-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/metaview/refs/heads/main/security/metaview-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/metaview-domain-security.yml
created: '2026-07-17'
description: Metaview is an AI-native, agentic recruiting platform used by more than 5,000 organizations to source, engage, and hire candidates. Its autonomous agents handle candidate sourcing, inbound application review against an Ideal Candidate Profile, AI interview notetaking purpose-built for recruiting, personalized outreach sequences, customizable recruiting reports, and job-post generation. Metaview integrates two-way with 60+ recruiting tools including ATS platforms (Ashby, Greenhouse, Lever, Gem, SmartRecruiters, Workday, SAP SuccessFactors), video conferencing (Zoom, Google Meet, Microsoft Teams), scheduling, and SSO providers. The company is backed by GV and Seedcamp. It exposes no public developer API today; this profile captures its identity, llms.txt, trust posture (SOC 2, GDPR), and domain security for the API Evangelist network.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/metaview.png
layout: provider
modified: '2026-10-06'
name: Metaview
nav: Providers
network: true
overview: 'Metaview is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Recruiting, Hiring, and Talent Acquisition.


  Metaview''s developer surface includes engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Metaview Plans Pricing
  plan_count: 5
  slug: metaview-plans-pricing
random_paper: 8
score:
  band: emerging
  composite: 22.9
  coverage:
    artifact_dirs: 8
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 6.3
  facets:
    access_clarity: 85.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 55.4
    operational_transparency: 0.0
  previous_composite: 16.6
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Employment & Payroll
    regime_id: employment_payroll
    score: 17.3
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/metaview/refs/heads/main/screenshots/metaview-2026-10-11T111046.png
security:
- kind: domain-security
  name: Metaview Domain Security
  slug: metaview-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Metaview Trust Center
  slug: metaview-trust-center
  summary_line: SOC 2, GDPR
slug: metaview
tags:
- Company
- Artificial Intelligence
- Recruiting
- Hiring
- Talent Acquisition
- AI Agents
- Interview Notes
- Human Resources
website: https://www.metaview.ai
---
