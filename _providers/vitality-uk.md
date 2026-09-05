---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
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
  score: 18.0
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: Vitality's production API gateway, running WSO2 API Manager at apis.vitality.co.uk (origin wso2-prd-apigw.tvc.vitality.co.uk:8243 behind an AWS load balancer in eu-west-1). The gateway is publicly res
  name: Vitality Partner API Gateway
  slug: vitality-partner-api-gateway
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vitality-uk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.vitality.co.uk/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/VitalityUK
- group: operate
  title: ''
  type: Contact
  url: https://www.vitality.co.uk/contact/
- group: operate
  title: ''
  type: Support
  url: https://www.vitality.co.uk/support/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.vitality.co.uk/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.vitality.co.uk/legal/
- group: auth
  title: ''
  type: Authentication
  url: authentication/vitality-uk-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/vitality-uk-scopes.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/vitality-uk-openid-configuration.json
- group: agent
  title: ''
  type: WellKnown
  url: well-known/vitality-uk-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/vitality-uk-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/vitality-uk-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/vitality-uk-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/vitality-uk-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/vitality-uk-llms.txt
created: '2026-07-25'
description: 'Vitality is a United Kingdom health and life insurer, operating as VitalityHealth and VitalityLife under the Vitality umbrella brand and owned by the South African financial services group Discovery Limited. Formed from the 2004 PruHealth joint venture with Prudential and the 2010 acquisition of Standard Life Healthcare, and rebranded to Vitality in 2014, it is the UK''s third-largest private medical insurer behind Bupa and AXA, with roughly 1.9 million members and a shared-value model that prices private medical insurance, life cover and protection against member health and activity engagement. Its lines of business are private medical insurance, life insurance and protection, and workplace/employee benefits distributed through intermediaries, employee benefit consultants and bank partnerships rather than direct developer channels. Vitality''s API posture is partner-gated and undocumented in public: it has modernised onto a WSO2 API Manager platform to decouple core policy
  and member services from front-end applications and to shorten partner onboarding, and it runs a publicly resolvable production API gateway at apis.vitality.co.uk, but it publishes no self-serve developer portal, no API reference, no OpenAPI or Swagger definitions and no public quote, bind, issue or FNOL endpoints. Credentials are issued through commercial partner onboarding and the gateway''s OAuth2 client-credentials token endpoint rejects anonymous callers. There is no public ACORD, AL3 or NGDS reference for the UK entity, which is consistent with a life-and-health carrier in a market where ACORD adoption is concentrated in the London subscription market rather than in retail health and protection.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-25'
name: Vitality
nav: Providers
network: true
overview: 'Vitality publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, United Kingdom, Health Insurance, Life Insurance, and Employee Benefits.


  Vitality''s developer surface includes support, authentication, and 14 more developer resources.'
random_paper: 0
scopes:
- name: Vitality Uk Scopes
  scope_count: 5
  slug: vitality-uk-scopes
  summary_line: 5 scopes · authorizationCode/clientCredentials
score:
  band: emerging
  composite: 23.1
  coverage:
    artifact_dirs: 10
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 23.1
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 63.6
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/vitality-uk/refs/heads/main/screenshots/vitality-uk-2026-09-02T170104.png
security:
- kind: authentication
  name: Vitality Uk Authentication
  slug: vitality-uk-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Vitality Uk Domain Security
  slug: vitality-uk-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: vitality-uk
tags:
- Insurance
- United Kingdom
- Health Insurance
- Life Insurance
- Employee Benefits
- Carrier
- Policy Administration
- Underwriting
- Partner Gated
website: https://www.vitality.co.uk/
---
