---
access_model:
  confidence: high
  label: Sales-gated
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://www.cognism.com/pricing
  - https://help.cognism.com/hc/en-gb/articles/37383359556498-API-Requirements-Entitlements
  - https://developers.cognism.com/
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: true
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
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
  score: 36.9
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Cognism Agentic Access
  operation_count: 25
  slug: cognism-agentic-access
  summary_line: 25 operations · 1 acting
api_count: 6
apis:
- description: Opt-out list lookups for GDPR/CCPA suppression.
  name: Cognism Compliance API
  slug: cognism-compliance-api
- description: Match a record you already hold to a Cognism record.
  name: Cognism Enrich API
  slug: cognism-enrich-api
- description: Read which fields your organisation is licensed for.
  name: Cognism Entitlement API
  slug: cognism-entitlement-api
- description: Reference lists of values the search filters accept.
  name: Cognism Filter API
  slug: cognism-filter-api
- description: Exchange a redeem ID for the full record.
  name: Cognism Redeem API
  slug: cognism-redeem-api
- description: Find contacts and companies matching a filter set.
  name: Cognism Search API
  slug: cognism-search-api
artifact_total: 48
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/cognism-api-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cognism-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cognism-authentication.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/cognism-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cognism-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cognism-domain-security.yml
- group: auth
  title: ''
  type: Security
  url: https://www.cognism.com/security
- group: auth
  title: ''
  type: Compliance
  url: https://www.cognism.com/compliance
- group: design
  title: ''
  type: Conformance
  url: conformance/cognism-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cognism-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cognism-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/cognism-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cognism-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Cognism
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cognism
- group: company
  title: ''
  type: Website
  url: https://www.cognism.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.cognism.com/
- group: operate
  title: ''
  type: Support
  url: https://help.cognism.com/hc/en-gb
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cognism.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.cognism.com/demo
- group: start
  title: ''
  type: Login
  url: https://app.cognism.com/auth/sign-in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cognism.com/terms-of-website-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cognism.com/privacy-policy
- group: commercial
  title: ''
  type: Plans
  url: plans/cognism-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cognism-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/cognism-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.cognism.com/blog/rss.xml
created: '2026-05-08'
description: 'Cognism is a B2B sales intelligence platform selling verified emails, mobile numbers, direct dials, firmographic and technographic data, buying-intent signals and contact enrichment to sales, marketing and RevOps teams, with a compliance-first posture built around GDPR and CCPA. Its API is a three-service REST contract published as a Postman collection at developers.cognism.com — a Search API for finding contacts and companies by filter, an Enrich API for matching records you already hold, and a Redeem API for exchanging the resulting redeem ID for the full profile. Search and Enrich return preview records and cost nothing; credits are consumed only when a contact is redeemed for the first time. A Compliance API exposes the opt-out suppression list, and an Entitlement API reports which fields the account is licensed to receive. API access is sales-gated: it must be enabled on the subscription, field-level entitlements provisioned by Cognism, and a six-month bearer token generated
  in the application.'
examples:
- key_count: 1
  name: Cognism Account Advanced Entitlement Response
  slug: cognism-account-advanced-entitlement-response
- key_count: 1
  name: Cognism Contact Advanced Entitlement Response
  slug: cognism-contact-advanced-entitlement-response
- key_count: 2
  name: Cognism Enrich Account By Domain Advanced Entitlement Response
  slug: cognism-enrich-account-by-domain-advanced-entitlement-response
- key_count: 2
  name: Cognism Enrich Account By Domain Standard Entitlement Response
  slug: cognism-enrich-account-by-domain-standard-entitlement-response
- key_count: 2
  name: Cognism Enrich Account By Linkedinurl Advanced Entitlement Response
  slug: cognism-enrich-account-by-linkedinurl-advanced-entitlement-response
- key_count: 2
  name: Cognism Enrich Account By Linkedinurl Standard Entitlement Response
  slug: cognism-enrich-account-by-linkedinurl-standard-entitlement-response
- key_count: 2
  name: Cognism Enrich Account By Various Standard Entitlement Response
  slug: cognism-enrich-account-by-various-standard-entitlement-response
- key_count: 2
  name: Cognism Enrich Account By Website Advanced Entitlement Response
  slug: cognism-enrich-account-by-website-advanced-entitlement-response
- key_count: 2
  name: Cognism Enrich Account By Website Standard Entitlement Response
  slug: cognism-enrich-account-by-website-standard-entitlement-response
- key_count: 1
  name: Cognism Enrich Account Request
  slug: cognism-enrich-account-request
- key_count: 2
  name: Cognism Enrich Accountby Various Advanced Entitlement Response
  slug: cognism-enrich-accountby-various-advanced-entitlement-response
- key_count: 2
  name: Cognism Enrich Contact By Email Advanced Entitlement Response
  slug: cognism-enrich-contact-by-email-advanced-entitlement-response
- key_count: 2
  name: Cognism Enrich Contact By Email Standard Entitlement Response
  slug: cognism-enrich-contact-by-email-standard-entitlement-response
- key_count: 2
  name: Cognism Enrich Contact By Firstname Lastname And Website Advanced Entitlement Response
  slug: cognism-enrich-contact-by-firstname-lastname-and-website-advanced-entitlement-response
- key_count: 2
  name: Cognism Enrich Contact By Firstname Lastname And Website Standard Entitlement Response
  slug: cognism-enrich-contact-by-firstname-lastname-and-website-standard-entitlement-response
- key_count: 2
  name: Cognism Enrich Contact By Linkedinurl Advanced Entitlement Response
  slug: cognism-enrich-contact-by-linkedinurl-advanced-entitlement-response
- key_count: 2
  name: Cognism Enrich Contact By Linkedinurl Standard Entitlement Response
  slug: cognism-enrich-contact-by-linkedinurl-standard-entitlement-response
- key_count: 2
  name: Cognism Enrich Contact By Phonenumber And Firstname Advanced Entitlement Response
  slug: cognism-enrich-contact-by-phonenumber-and-firstname-advanced-entitlement-response
- key_count: 2
  name: Cognism Enrich Contact By Phonenumber And Firstname Standard Entitlement Response
  slug: cognism-enrich-contact-by-phonenumber-and-firstname-standard-entitlement-response
- key_count: 2
  name: Cognism Enrich Contact By Various Advanced Entitlement Response
  slug: cognism-enrich-contact-by-various-advanced-entitlement-response
- key_count: 2
  name: Cognism Enrich Contact By Various Standard Entitlement Response
  slug: cognism-enrich-contact-by-various-standard-entitlement-response
- key_count: 1
  name: Cognism Enrich Contact Request
  slug: cognism-enrich-contact-request
- key_count: 1
  name: Cognism Redeem Accounts By Ids Request
  slug: cognism-redeem-accounts-by-ids-request
- key_count: 2
  name: Cognism Redeem Advanced Entitlement Response
  slug: cognism-redeem-advanced-entitlement-response
- key_count: 2
  name: Cognism Redeem Contact Advanced Entitlement Response
  slug: cognism-redeem-contact-advanced-entitlement-response
- key_count: 2
  name: Cognism Redeem Contact Standard Entitlement Response
  slug: cognism-redeem-contact-standard-entitlement-response
- key_count: 1
  name: Cognism Redeem Contacts By Ids Request
  slug: cognism-redeem-contacts-by-ids-request
- key_count: 2
  name: Cognism Redeem Standard Entitlement Response
  slug: cognism-redeem-standard-entitlement-response
- key_count: 3
  name: Cognism Search Account Advanced Entitlement Response
  slug: cognism-search-account-advanced-entitlement-response
- key_count: 3
  name: Cognism Search Account Standard Entitlement Response
  slug: cognism-search-account-standard-entitlement-response
- key_count: 3
  name: Cognism Search Accounts Request
  slug: cognism-search-accounts-request
- key_count: 3
  name: Cognism Search Contacts Advanced Entitlement Response
  slug: cognism-search-contacts-advanced-entitlement-response
- key_count: 8
  name: Cognism Search Contacts Request
  slug: cognism-search-contacts-request
- key_count: 3
  name: Cognism Search Contacts Standard Entitlement Response
  slug: cognism-search-contacts-standard-entitlement-response
finops:
- name: Cognism Finops
  service_category: Sales Intelligence
  slug: cognism-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cognism.png
layout: provider
modified: '2026-08-13'
name: Cognism
nav: Providers
network: true
overview: 'Cognism publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Compliance API, Enrich API, Entitlement API, and 3 more. Tagged areas include Sales Intelligence, B2B, Enrichment, Contact Data, and GDPR.


  Cognism''s developer surface includes authentication, support, pricing, signup flow, engineering blog, and 23 more developer resources.'
plans:
- name: Cognism Plans Pricing
  plan_count: 4
  slug: cognism-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 3
  name: Cognism Rate Limits
  slug: cognism-rate-limits
score:
  band: developing
  composite: 51.6
  coverage:
    artifact_dirs: 22
    catalog_gap: 48.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 100.0
    commercial_clarity: 100.0
    contract_governance: 4.5
    contract_quality: 17.4
    developer_ergonomics: 63.7
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 44.7
  previous_composite: 51.6
  provenance:
    agentic_access: first-party
    conformance: derived
    contracts:
      callable: 100.0
      derived: 7
      marker_coverage: 100.0
      total: 7
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cognism/refs/heads/main/screenshots/cognism-2026-06-20T174713.png
security:
- kind: authentication
  name: Cognism Authentication
  slug: cognism-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Cognism Domain Security
  slug: cognism-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Cognism Vulnerability Disclosure
  slug: cognism-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Cognism Trust Center
  slug: cognism-trust-center
  summary_line: SOC 2, ISO 27001
slug: cognism
tags:
- Sales Intelligence
- B2B
- Enrichment
- Contact Data
- GDPR
- Intent Data
- Lead Generation
- Firmographics
- Technographics
- Company Data
- Prospecting
- Data as a Service
website: https://www.cognism.com/
---
