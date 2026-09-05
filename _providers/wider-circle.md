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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 5
common:
- group: commercial
  title: ''
  type: Plans
  url: plans/wider-circle-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/wider-circle-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/wider-circle-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/wider-circle-conformance.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/wider-circle-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: https://policy.widercircle.com/
- group: auth
  title: ''
  type: Compliance
  url: https://www.widercircle.com/health-plans/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/wider-circle-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wider-circle-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.widercircle.com/
- group: company
  title: ''
  type: About
  url: https://www.widercircle.com/about/
- group: company
  title: ''
  type: Blog
  url: https://www.widercircle.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.widercircle.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://www.widercircle.com/contact/
- group: start
  title: ''
  type: SignUp
  url: https://www.widercircle.com/sign-up/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.widercircle.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.widercircle.com/privacy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/WiderCircle
coverage:
  checked: '2026-09-04'
  detail: 'Wider Circle runs a real technology platform behind its Connect for Life community-health program, but exposes none of it: the 94-URL page sitemap contains no developer, docs or API page, api.widercircle.com resolves to a CloudFront distribution that has no certificate for that hostname and answers 403 behind it, and the only two authenticated surfaces are a Salesforce Experience Cloud FacilitatorLogin and a help-centre login shell.'
  evidence:
  - status: 403
    url: https://api.widercircle.com/
  - status: 200
    url: https://www.widercircle.com/page-sitemap.xml
  - status: 200
    url: https://portal.widercircle.com/
  - status: 404
    url: https://www.widercircle.com/openapi.json
  - status: 404
    url: https://www.widercircle.com/.well-known/agent-card.json
  reason: no-developer-program
  state: none
created: '2026-09-04'
description: Wider Circle is a Redwood City, California community-health company that partners with Medicare Advantage, Medicaid and D-SNP health plans to close the "last mile" of care through peer-driven neighborhood groups. Its Connect for Life program clusters plan members by claims-derived affinity, recruits and trains local Ambassadors and Facilitators, and runs in-person and virtual group programming aimed at annual wellness visits, CAHPS and Star Ratings, medication adherence, social isolation and social determinants of health. The technology stack behind the model is operated as an internal platform and a Salesforce Experience Cloud facilitator portal; as of this profile Wider Circle publishes no public developer program, API documentation, or machine-readable API contract of any kind.
image: https://www.widercircle.com/wp-content/uploads/2021/08/wider-circle-logo-2021.svg
layout: provider
modified: '2026-09-04'
name: Wider Circle
nav: Providers
network: true
overview: 'Wider Circle is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Health Plans, Medicare Advantage, and Medicaid.


  Wider Circle''s developer surface includes engineering blog, support, signup flow, and 15 more developer resources.'
plans:
- name: Wider Circle Plans Pricing
  plan_count: 0
  slug: wider-circle-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Wider Circle Rate Limits
  slug: wider-circle-rate-limits
score:
  band: emerging
  composite: 24.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 15.8
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 45.0
  schema_version: 0.18.3
  scored_at: '2026-09-04'
security:
- kind: domain-security
  name: Wider Circle Domain Security
  slug: wider-circle-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Wider Circle Vulnerability Disclosure
  slug: wider-circle-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Wider Circle Trust Center
  slug: wider-circle-trust-center
  summary_line: HITRUST CSF Certification, HIPAA
slug: wider-circle
tags:
- Company
- Healthcare
- Health Plans
- Medicare Advantage
- Medicaid
- Population Health
- Social Determinants of Health
- Member Engagement
- Care Coordination
- Community Health
website: https://www.widercircle.com/
---
