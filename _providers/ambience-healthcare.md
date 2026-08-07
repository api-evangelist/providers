---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 12.6
  scored_at: '2026-08-06'
api_count: 2
apis:
- description: 'Partner-facing integration APIs for EHRs, telehealth platforms and healthcare applications, covering medical encounter transcription, clinical note generation, integrated CDI with ICD-10 suggestions, '
  name: Ambience Integration API
  slug: ambience-integration-api
- description: The OpenID Connect provider fronting the Ambience application and API platform. Publishes an RFC 8414 / OIDC Discovery document anonymously at /.well-known/openid-configuration, advertising authorizat
  name: Ambience Identity (OAuth 2.0 / OpenID Connect)
  slug: ambience-identity-oauth-20-openid-connect
artifact_total: 6
common:
- group: auth
  title: ''
  type: Authentication
  url: authentication/ambience-healthcare-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/ambience-healthcare-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ambience-healthcare-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ambience-healthcare-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/ambience-healthcare-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ambience-healthcare-llms.txt
- group: auth
  title: ''
  type: TrustCenter
  url: security/ambience-healthcare-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ambience-healthcare-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ambiencehealthcare.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.ambiencehealthcare.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ambiencehealthcare.com/
- group: company
  title: ''
  type: Blog
  url: https://www.ambiencehealthcare.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Ambience-Healthcare
- group: start
  title: ''
  type: SignUp
  url: https://www.ambiencehealthcare.com/demo
- group: start
  title: ''
  type: Login
  url: https://app.ambiencehealthcare.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ambiencehealthcare.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cdn.prod.website-files.com/65be6ed75db0972f744bb6b1/65c1a3f7d8cbb7b2397bd541_63fd4608cf1aa8041a98d378_terms.pdf
- group: auth
  title: ''
  type: Compliance
  url: https://www.ambiencehealthcare.com/informatics
- group: company
  title: ''
  type: Careers
  url: https://www.ambiencehealthcare.com/careers
- group: other
  title: ''
  type: CustomerStories
  url: https://www.ambiencehealthcare.com/customer-stories
- group: other
  title: ''
  type: Products
  url: https://www.ambiencehealthcare.com/products
created: '2026-07-31'
description: 'Ambience Healthcare is a San Francisco based ambient clinical AI company whose platform listens to the patient encounter and produces documentation, coding and revenue-cycle output for health systems. Its products include AutoScribe (ambient AI medical scribe tuned to 100+ specialties and subspecialties), AutoCDI, AutoAVS, AutoRefer, AutoPrep, a Chart Awareness layer and a nursing suite. Ambience runs inside the EHR rather than beside it: it is distributed through the Epic Toolbox (Hyperspace and Haiku) using SMART on FHIR, through the athenahealth Marketplace, and into Oracle Cerner Millennium over FHIR and REST APIs, reading patient context from the chart and writing structured notes, codes and summaries back. The company also publishes a partner-facing Integration API programme at docs.ambiencehealthcare.com for EHRs, telehealth platforms and healthcare applications covering encounter transcription, note generation, CDI with ICD-10 suggestion and chart context enrichment,
  with access granted on request rather than through public self-service signup.'
image: https://framerusercontent.com/images/l2jbzG0Wzk7GJYt31m2QzU82JzQ.png
layout: provider
modified: '2026-07-31'
name: Ambience Healthcare
nav: Providers
network: true
overview: 'Ambience Healthcare publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Artificial Intelligence, Clinical Documentation, and Ambient AI.


  Ambience Healthcare''s developer surface includes authentication, documentation, engineering blog, signup flow, and 17 more developer resources.'
random_paper: 98
scopes:
- name: Ambience Healthcare Scopes
  scope_count: 14
  slug: ambience-healthcare-scopes
  summary_line: 14 scopes · authorizationCode/clientCredentials/deviceCode
score:
  band: thin
  composite: 33.6
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 30.4
    discoverability: 77.8
    governance: 12.5
    operational_transparency: 5.3
  previous_composite: 33.6
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 76.3
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Ambience Healthcare Authentication
  slug: ambience-healthcare-authentication
  summary_line: openIdConnect/oauth2 · 2 schemes
- kind: domain-security
  name: Ambience Healthcare Domain Security
  slug: ambience-healthcare-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Ambience Healthcare Trust Center
  slug: ambience-healthcare-trust-center
  summary_line: HIPAA
slug: ambience-healthcare
tags:
- Company
- Healthcare
- Artificial Intelligence
- Clinical Documentation
- Ambient AI
- Medical Coding
- Electronic Health Records
- FHIR
- Health IT
- Speech Recognition
website: https://www.ambiencehealthcare.com/
---
