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
  url: https://radicalhealth.ai/
- group: start
  title: ''
  type: SignUp
  url: https://platform.radicalhealth.ai/register
- group: start
  title: ''
  type: Login
  url: https://platform.radicalhealth.ai/login
- group: commercial
  title: ''
  type: Pricing
  url: https://radicalhealth.ai/
- group: company
  title: ''
  type: Blog
  url: https://radicalhealth.ai/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://platform.radicalhealth.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://platform.radicalhealth.ai/privacy-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/radicalhealth-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/radicalhealth-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/radicalhealth-security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/radicalhealth-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/radicalhealth-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://radicalhealth.ai/.well-known/security.txt
- group: auth
  title: ''
  type: TrustCenter
  url: security/radicalhealth-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: security/radicalhealth-trust-center.yml
created: '2026-07-17'
description: Radical Health is a Khosla Ventures-backed healthcare AI company that produces personalized, expert-reviewed cancer treatment reports for patients in the United States. Its platform ingests a patient's medical records and synthesizes oncology research, clinical trials, and prior patient outcomes into a tailored report within days, drawing on 5.3 million research papers, 11.8 million patient journeys, 20,000 treatment options, and 48,800+ active US clinical trials. The service pairs an always-on AI nurse navigator ("Alice") with human oncology oversight from institutions including UCLA, Johns Hopkins, Stanford, and Kaiser Permanente, and connects to 70,000+ US healthcare institutions (Epic, Kaiser, Ascension, HCA, Medicare) for records access. Reports are informational and educational only, not medical advice. Radical Health is HIPAA and SOC 2 Type II certified and operates as a consumer subscription product ($110/month with a 7-day free trial); it does not currently publish
  a public developer API, SDK, or OpenAPI surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/radicalhealth.png
layout: provider
modified: '2026-07-20'
name: Radical Health
nav: Providers
network: true
overview: 'Radical Health is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Oncology, Artificial Intelligence, and Clinical Trials.


  Radical Health''s developer surface includes signup flow, pricing, engineering blog, and 12 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 14.6
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 32.9
    commercial_clarity: 32.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 14.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 21.3
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/radicalhealth/refs/heads/main/screenshots/radicalhealth-2026-09-02T152754.png
security:
- kind: domain-security
  name: Radicalhealth Domain Security
  slug: radicalhealth-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Radicalhealth Vulnerability Disclosure
  slug: radicalhealth-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Radicalhealth Trust Center
  slug: radicalhealth-trust-center
  summary_line: HIPAA, SOC 2 Type II
slug: radicalhealth
tags:
- Company
- Healthcare
- Oncology
- Artificial Intelligence
- Clinical Trials
- Patient Care
- Digital Health
website: https://radicalhealth.ai/
---
