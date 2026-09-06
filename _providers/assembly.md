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
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/assembly-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/assembly-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: security/assembly-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/assembly-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.joinassembly.com/security-policy
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/assembly-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://www.joinassembly.com/status
- group: commercial
  title: ''
  type: Pricing
  url: https://www.joinassembly.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://help.joinassembly.com
- group: company
  title: ''
  type: Blog
  url: https://www.joinassembly.com/press
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.joinassembly.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.joinassembly.com/privacy-policy
- group: start
  title: ''
  type: SignUp
  url: https://www.joinassembly.com/book-demo
- group: company
  title: ''
  type: Website
  url: https://www.joinassembly.com
created: '2026-07-17'
description: Assembly (joinassembly.com, by Quantum Workplace) is an employee recognition, rewards, and engagement platform that helps organizations celebrate achievements, run peer-to-peer recognition, milestone and anniversary celebrations, custom awards, challenges, and an integrated rewards catalog to build company culture. Assembly connects to the HR and communications stack through 80+ prebuilt integrations (Slack, Microsoft Teams, BambooHR, Workday, ADP, Rippling, Okta, Google Workspace, and more). Assembly does not publish a self-service developer REST API; integration is via its prebuilt connector catalog. It was surfaced in the API Evangelist network as a portfolio company of Homebrew, Union Square Ventures, and Y Combinator.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/assembly.png
layout: provider
modified: '2026-07-18'
name: Assembly
nav: Providers
network: true
overview: 'Assembly is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Developer Tools, Employee Recognition, Employee Engagement, and Rewards.


  Assembly''s developer surface includes pricing, support, engineering blog, signup flow, and 10 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 21.9
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 21.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/assembly/refs/heads/main/screenshots/assembly-2026-07-25T201440.png
security:
- kind: domain-security
  name: Assembly Domain Security
  slug: assembly-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Assembly Vulnerability Disclosure
  slug: assembly-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Assembly Trust Center
  slug: assembly-trust-center
  summary_line: SOC 2 Type II, ISO 27001, PCI DSS Level 1, GDPR, CCPA
slug: assembly
tags:
- Company
- Developer Tools
- Employee Recognition
- Employee Engagement
- Rewards
- Human Resources
- Workplace
- Software-as-a-Service
- Integration
website: https://www.joinassembly.com
---
