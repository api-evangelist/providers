---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.0
  scored_at: '2026-08-06'
api_count: 1
apis:
- description: The private REST API behind the Forta Health clinical operations platform (app.fortahealth.com), a FastAPI service exposing 450 operations across 306 paths covering providers and provider assignments,
  name: Forta Health Clinical Operations API
  slug: forta-health-clinical-operations-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.fortahealth.com/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://www.hiive.com/securities/forta-health-stock
- group: start
  title: ''
  type: SignUp
  url: https://www.fortahealth.com/contact
- group: start
  title: ''
  type: Login
  url: https://app.fortahealth.com/
- group: operate
  title: ''
  type: Support
  url: https://www.fortahealth.com/contact
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.fortahealth.com/faq
- group: company
  title: ''
  type: Blog
  url: https://www.fortahealth.com/resources
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.fortahealth.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.fortahealth.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fortahealth
- group: other
  title: ''
  type: Research
  url: https://www.fortahealth.com/our-research
- group: company
  title: ''
  type: Careers
  url: https://www.fortahealth.com/careers
- group: auth
  title: ''
  type: Compliance
  url: https://www.fortahealth.com/notice-of-privacy-practices
- group: design
  title: ''
  type: Conformance
  url: conformance/forta-health-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/forta-health-packages.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/forta-health-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/forta-health-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/forta-health-llms.txt
created: '2026-08-04'
description: 'Forta Health operates the largest virtual Applied Behavior Analysis (ABA) network in the United States, delivering autism therapy to children through two models: Virtual ABA over a HIPAA-secure telehealth platform across 43 states, and In-Home ABA in Dallas, Houston and San Antonio, Texas. Founded in 2021 and led by CEO Edan Morag, Forta pairs Board Certified Behavior Analysts (BCBAs) who design and supervise individualized treatment plans with Registered Behavior Technicians (RBTs) and trained parents who deliver live sessions, using proprietary software and machine-learning models that ingest medical records and session data to surface relevant case data for clinicians and personalize each treatment plan. The company works with major commercial payers and state Medicaid programs to shorten the typical six-to-eighteen-month ABA waitlist to roughly ninety days. Forta publishes no public developer program; its clinical operations platform is a private, bearer-token-authenticated
  REST API.'
image: https://cdn.prod.website-files.com/62605ac6c670d21352ebb32c/675d0e02ce1be8abd64c0749_opengraph.webp
layout: provider
modified: '2026-08-04'
name: Forta Health
nav: Providers
network: true
overview: 'Forta Health publishes 1 API on the [APIs.io](https://apis.io/) network: Clinical Operations API. Tagged areas include healthcare, autism, aba-therapy, behavioral-health, and telehealth.


  Forta Health''s developer surface includes signup flow, support, engineering blog, and 15 more developer resources.'
random_paper: 85
score:
  band: thin
  composite: 32.8
  delta: 0.0
  facets:
    commercial_clarity: 42.1
    contract_quality: 51.2
    developer_ergonomics: 6.5
    discoverability: 87.0
    governance: 11.5
    operational_transparency: 5.3
  previous_composite: 32.8
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 30.0
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Forta Health Authentication
  slug: forta-health-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Forta Health Domain Security
  slug: forta-health-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: forta-health
tags:
- healthcare
- autism
- aba-therapy
- behavioral-health
- telehealth
- digital-health
- pediatric-care
- clinical-operations
- medicaid
- health-insurance
- ehr
- machine-learning
website: https://www.fortahealth.com/
---
