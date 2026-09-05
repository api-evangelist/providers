---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Google Recaptcha Agentic Access
  operation_count: 6
  slug: google-recaptcha-agentic-access
  summary_line: 6 operations · 4 acting
api_count: 1
apis:
- description: The reCAPTCHA Site Verify API is the standard verification endpoint for reCAPTCHA v2 and v3 tokens. After a user completes a reCAPTCHA challenge on the frontend, the backend sends the response token t
  name: reCAPTCHA Site Verify API
  slug: recaptcha-site-verify-api
- baseURL: https://recaptchaenterprise.googleapis.com
  baseurl_source: declared
  description: Create and annotate risk assessments
  name: Google reCAPTCHA Assessments API
  slug: google-recaptcha-assessments-api
- baseURL: https://recaptchaenterprise.googleapis.com
  baseurl_source: declared
  description: Manage reCAPTCHA site keys
  name: Google reCAPTCHA Keys API
  slug: google-recaptcha-keys-api
artifact_total: 20
collections:
- collection_type: postman
  name: Google reCAPTCHA reCAPTCHA Enterprise Assessments API
  slug: postman-google-recaptcha-assessments-api
- collection_type: postman
  name: Google reCAPTCHA reCAPTCHA Enterprise Assessments Keys API
  slug: postman-google-recaptcha-keys-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Google reCAPTCHA reCAPTCHA Enterprise Assessments API
  slug: open-google-recaptcha-assessments-api
- collection_type: open
  name: Google reCAPTCHA reCAPTCHA Enterprise Assessments Keys API
  slug: open-google-recaptcha-keys-api
- collection_type: open
  name: Google reCAPTCHA reCAPTCHA Enterprise API
  slug: open-recaptcha-enterprise
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-recaptcha/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-recaptcha-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-recaptcha-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-recaptcha-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-recaptcha-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-recaptcha-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/google
- group: start
  title: ''
  type: GettingStarted
  url: https://cloud.google.com/recaptcha-enterprise/docs/getting-started
- group: commercial
  title: ''
  type: Pricing
  url: https://cloud.google.com/recaptcha-enterprise/pricing
- group: auth
  title: ''
  type: Authentication
  url: https://cloud.google.com/recaptcha-enterprise/docs/authentication
- group: start
  title: ''
  type: Console
  url: https://console.cloud.google.com/security/recaptcha
- group: build
  title: ''
  type: SDKs
  url: https://cloud.google.com/recaptcha-enterprise/docs/libraries
- group: operate
  title: ''
  type: Support
  url: https://cloud.google.com/recaptcha-enterprise/docs/support
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloud.google.com
- group: design
  title: ''
  type: JSONLD
  url: json-ld/google-recaptcha-context.jsonld
created: '2026-03-13'
description: Google reCAPTCHA is a security service that protects websites and applications from spam and abuse by verifying that interactions are from real humans rather than bots, offering Enterprise and standard APIs for site verification and risk assessment.
finops:
- name: Google Recaptcha Finops
  service_category: API
  slug: google-recaptcha-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-recaptcha.png
json_schemas:
- name: reCAPTCHA Enterprise Assessment
  property_count: 4
  slug: google-recaptcha-assessment
jsonld:
- class_count: 0
  name: Google Recaptcha Context
  property_count: 3
  slug: google-recaptcha-context
layout: provider
modified: '2026-05-19'
name: Google reCAPTCHA
nav: Providers
network: true
overview: 'Google reCAPTCHA publishes 2 APIs on the [APIs.io](https://apis.io/) network: Assessments API and Keys API. Tagged areas include Abuse Prevention, Bot Detection, CAPTCHA, Fraud Prevention, and Google Cloud.


  The Google reCAPTCHA catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google reCAPTCHA''s developer surface includes authentication, getting-started guide, pricing, developer console, support, and 10 more developer resources.'
plans:
- name: Google Recaptcha Plans Pricing
  plan_count: 3
  slug: google-recaptcha-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 5
  name: Google Recaptcha Rate Limits
  slug: google-recaptcha-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Google reCAPTCHA API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-recaptcha-jsonschema-spectral-rules
scopes:
- name: Google Recaptcha Scopes
  scope_count: 1
  slug: google-recaptcha-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 41.8
  coverage:
    artifact_dirs: 14
    catalog_earned: 60.3
    catalog_earned_first_party: 0.0
    catalog_gap: 54.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 9.8
    contract_quality: 63.3
    developer_ergonomics: 46.4
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 26.3
  previous_composite: 42.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-recaptcha/refs/heads/main/screenshots/google-recaptcha-2026-06-20T182229.png
security:
- kind: authentication
  name: Google Recaptcha Authentication
  slug: google-recaptcha-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Recaptcha Domain Security
  slug: google-recaptcha-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Recaptcha Vulnerability Disclosure
  slug: google-recaptcha-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-recaptcha
tags:
- Abuse Prevention
- Bot Detection
- CAPTCHA
- Fraud Prevention
- Google Cloud
- Security
---
