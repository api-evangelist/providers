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
artifact_total: 2
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/lingokids-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lingokids-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://lingokids.com/
- group: operate
  title: ''
  type: Support
  url: https://help.lingokids.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://lingokids.com/news
- group: company
  title: ''
  type: BlogRSS
  url: https://lingokids.com/feed
- group: commercial
  title: ''
  type: Pricing
  url: https://store.lingokids.com/
- group: start
  title: ''
  type: SignUp
  url: https://app.lingokids.com/users/new
- group: commercial
  title: ''
  type: TermsOfService
  url: https://lingokids.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://lingokids.com/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://lingokids.com/privacy-policy
- group: operate
  title: ''
  type: Contact
  url: https://lingokids.com/contact
- group: company
  title: ''
  type: Press
  url: https://lingokids.com/press
- group: company
  title: ''
  type: Careers
  url: https://jobs.lingokids.com/
- group: other
  title: ''
  type: Teachers
  url: https://lingokids.com/teachers
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lingokids
- group: agent
  title: ''
  type: WellKnown
  url: well-known/lingokids-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/lingokids-security.txt
- group: auth
  title: ''
  type: Security
  url: https://lingokids.com/.well-known/security.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/lingokids-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/lingokids-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lingokids-llms.txt
created: '2026-07-17'
description: 'Lingokids is a children''s edutainment platform operated by Monkimun Inc. (Wilmington, Delaware) and Monkimun Labs S.L. (Madrid, Spain), delivering an ad-free "Playlearning" experience of games, animated shows, podcasts and sing-alongs for children aged two to eight. The mobile apps (iOS, Android, Amazon) and web app have been downloaded more than 200 million times. The curriculum is built by parents and educators and covers English-language learning alongside broader academic and life skills. Lingokids is audited and certified by the kidSAFE Seal Program (COPPA+), operates a COPPA-compliant configuration for child data, and honours GDPR rights for EU residents. The company publishes no public developer program or documented API: api.lingokids.com is the private application backend and exposes no discovery surface. Lingokids does publish an RFC 9116 security.txt with a security contact, names a Data Protection Officer, and runs a public help center. Backed by HV Capital.'
image: https://lingokids.com/wp-content/uploads/2026/06/cropped-Lingokids_Facebook_Avatar-1-192x192.png
layout: provider
modified: '2026-07-19'
name: Lingokids
nav: Providers
network: true
overview: 'Lingokids is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Education, EdTech, and Children.


  Lingokids'' developer surface includes support, engineering blog, pricing, signup flow, and 18 more developer resources.'
random_paper: 19
score:
  band: emerging
  composite: 25.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 7.9
  previous_composite: 25.1
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 55.6
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lingokids/refs/heads/main/screenshots/lingokids-2026-07-25T225243.png
security:
- kind: domain-security
  name: Lingokids Domain Security
  slug: lingokids-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Lingokids Vulnerability Disclosure
  slug: lingokids-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: lingokids
tags:
- Company
- Consumer
- Education
- EdTech
- Children
- Language Learning
- Mobile Apps
- Spain
website: https://lingokids.com/
---
