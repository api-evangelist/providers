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
api_count: 1
apis:
- description: RESTful API for submitting files, generating Similarity Reports, and displaying integrity results inside a host learning management system or environment. Reference documentation is credential-gated t
  name: Turnitin Core API (TCA)
  slug: turnitin-core-api-tca
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.turnitin.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.turnitin.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.turnitin.com/turnitin-core-api
- group: docs
  title: ''
  type: APIReference
  url: https://developers.turnitin.com/turnitin-core-api/documentation
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.turnitin.com/turnitin-core-api
- group: company
  title: ''
  type: Blog
  url: https://www.turnitin.com/blog/
- group: operate
  title: ''
  type: HelpCenter
  url: https://helpcenter.turnitin.com/
- group: operate
  title: ''
  type: Support
  url: https://support.turnitin.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://turnitin.statuspage.io/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.turnitin.com/privacy-policy-website/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.turnitin.com/terms-of-use-website/
- group: auth
  title: ''
  type: Security
  url: https://www.turnitin.com/vulnerability-disclosure-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://developers.turnitin.com/turnitin-core-api
- group: design
  title: ''
  type: Conformance
  url: conformance/turnitin-iparadigms-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/turnitin-iparadigms-lifecycle.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/turnitin-iparadigms-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/turnitin-iparadigms-domain-security.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/turnitin-iparadigms-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/turnitin-iparadigms-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/turnitin-iparadigms-llms.txt
created: '2026-07-17'
description: 'Turnitin (iParadigms) is an education-technology company providing academic integrity, similarity checking, and grading products used by schools, universities, researchers, and publishers worldwide. Turnitin exposes two programmatic integration surfaces for third-party platforms: a 1EdTech-certified Learning Tools Interoperability (LTI 1.3 / LTI Advantage) integration, and the Turnitin Core API (TCA) — a RESTful API that lets a platform submit files, generate Similarity Reports, and display results in-workflow without leaving the host learning environment. The TCA reference documentation is credential-gated; access is granted to existing customers and approved integration partners. Turnitin states SOC 2 compliance and operates international data centers. Gradescope is a Turnitin company. Backed by Insight Partners.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/turnitin-iparadigms.png
layout: provider
modified: '2026-07-21'
name: Turnitin (iParadigms)
nav: Providers
network: true
overview: 'Turnitin (iParadigms) publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Education, EdTech, Academic Integrity, and Plagiarism Detection.


  Turnitin (iParadigms)''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, and 15 more developer resources.'
random_paper: 0
score:
  band: thin
  composite: 29.9
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 38.1
    discoverability: 66.7
    governance: 18.2
    operational_transparency: 26.3
  previous_composite: 29.9
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
screenshot: https://raw.githubusercontent.com/api-evangelist/turnitin-iparadigms/refs/heads/main/screenshots/turnitin-iparadigms-2026-09-02T164542.png
security:
- kind: domain-security
  name: Turnitin Iparadigms Domain Security
  slug: turnitin-iparadigms-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Turnitin Iparadigms Vulnerability Disclosure
  slug: turnitin-iparadigms-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: turnitin-iparadigms
tags:
- Company
- Education
- EdTech
- Academic Integrity
- Plagiarism Detection
- Similarity
- LTI
- Assessment
- Grading
website: https://www.turnitin.com/
---
