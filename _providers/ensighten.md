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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.8
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: 'The REST Manage API used by Ensighten Manage customers to administer tag management programmatically. Sixty-six operations covering Spaces, Publish Paths, Deployments (create, update, enable/disable, '
  name: Ensighten Manage API
  slug: manage-api
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://cheq.ai/ensighten/
- group: start
  title: ''
  type: Login
  url: https://manage.ensighten.com/
- group: operate
  title: ''
  type: Support
  url: https://help.ensighten.com/hc/en-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.ensighten.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://cheq.ai/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cheq.ai/cheq-terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cheq.ai/website-privacy-policy/
- group: auth
  title: ''
  type: TrustCenter
  url: https://cheq.ai/trust/
- group: auth
  title: ''
  type: Compliance
  url: https://cheq.ai/trust/
- group: auth
  title: ''
  type: TrustCenter
  url: security/ensighten-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ensighten-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://manageexternalapi.docs.apiary.io/
- group: docs
  title: ''
  type: APIReference
  url: https://manageexternalapi.docs.apiary.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.ensighten.com/hc/en-us/sections/22957479812369
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Ensighten
- group: build
  title: ''
  type: Packages
  url: packages/ensighten-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/ensighten-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ensighten-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ensighten-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/ensighten-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/ensighten-plans-pricing.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/ensighten-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ensighten-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ensighten-data-model.yml
created: '2026-07-17'
description: 'Ensighten is an enterprise tag management, data governance, and client-side website security platform. It gives digital, marketing, and privacy teams centralized control over the third-party tags, scripts, and vendor code that run on their web and mobile properties, enforcing consent and privacy rules (GDPR, CCPA) at the point of data collection. The platform combines server- and client-side tag management, malicious-script and data-leakage detection (client-side security), and consent management. Ensighten was acquired by CHEQ (CHEQ AI Technologies Ltd.) and is now delivered as part of CHEQ''s Control & Compliance / Go-to-Market Security suite; the ensighten.com domain 301-redirects to cheq.ai. This company profile was surfaced as an Insight Partners portfolio lead and enriched by the API Evangelist pipeline. Ensighten does publish a public REST contract: the Ensighten Manage API, documented as an API Blueprint at manageexternalapi.docs.apiary.io and served in production from
  manage-api.ensighten.com. It covers 66 operations across Spaces, Publish Paths, Deployments, Conditions, Data Definitions, Event Definitions, Labels, Users, Roles, SCIM 2.0 user/group provisioning, Git-enabled spaces, and TDN jobs. Authentication is either an X-API-Key API key or an OAuth 2.0 Resource Owner Password Credentials bearer token from /auth/token.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ensighten.png
layout: provider
modified: '2026-08-13'
name: Ensighten
nav: Providers
network: true
overview: 'Ensighten publishes 1 API on the [APIs.io](https://apis.io/) network: Manage API. Tagged areas include Company, Cybersecurity, Tag Management, Data Governance, and Client-Side Security.


  Ensighten''s developer surface includes support, engineering blog, documentation, API reference, getting-started guide, changelog, and 19 more developer resources.'
plans:
- name: Ensighten Plans Pricing
  plan_count: 0
  slug: ensighten-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 1
  name: Ensighten Rate Limits
  slug: ensighten-rate-limits
score:
  band: developing
  composite: 50.5
  delta: 3.8
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 30.3
    contract_quality: 56.5
    developer_ergonomics: 55.4
    discoverability: 68.5
    governance: 30.3
    operational_transparency: 47.4
  previous_composite: 46.7
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ensighten/refs/heads/main/screenshots/ensighten-2026-07-25T213419.png
security:
- kind: authentication
  name: Ensighten Authentication
  slug: ensighten-authentication
  summary_line: apiKey/http/oauth2 · 3 schemes
- kind: domain-security
  name: Ensighten Domain Security
  slug: ensighten-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Ensighten Trust Center
  slug: ensighten-trust-center
  summary_line: SOC 2 Type II, ISO 27001, ISO 27701, ISO 42001, CSA STAR Level 1, GDPR, CCPA
slug: ensighten
tags:
- Company
- Cybersecurity
- Tag Management
- Data Governance
- Client-Side Security
- Consent Management
- Privacy Compliance
- Marketing Technology
website: https://cheq.ai/ensighten/
---
