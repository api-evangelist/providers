---
agent_readiness:
  band: agent-ready
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
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.4
  scored_at: '2026-10-17'
api_count: 4
apis:
- description: Checkout API provides payment processing endpoints as documented in the API reference.
  name: Checkout API
  slug: checkout-api-2
- description: The Checkout API API from Checkout — 1 operation(s) for checkout api.
  name: Checkout Checkout API
  slug: checkout-checkout-api-api
- description: The Connect API from Checkout — 1 operation(s) for connect.
  name: Checkout Connect API
  slug: checkout-connect-api
- description: The Payments API from Checkout — 1 operation(s) for payments.
  name: Checkout Payments API
  slug: checkout-payments-api
artifact_total: 11
asyncapis:
- description: ''
  name: Checkout Webhooks
  slug: checkout-webhooks
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/checkout/refs/heads/main/rules/checkout-rules.yml
  title: ''
  type: Spectral
  url: rules/checkout-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/checkout/refs/heads/main/json-ld/checkout-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/checkout-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/checkout/refs/heads/main/vocabulary/checkout-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/checkout-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/checkout/refs/heads/main/asyncapi/checkout-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/checkout-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/checkout/refs/heads/main/data-model/checkout-data-model.yml
  title: ''
  type: DataModel
  url: data-model/checkout-data-model.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/checkout/refs/heads/main/security/checkout-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/checkout-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/checkout/refs/heads/main/authentication/checkout-authentication.yml
  title: ''
  type: Authentication
  url: authentication/checkout-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/checkout/refs/heads/main/conformance/checkout-conformance.yml
  title: ''
  type: Conformance
  url: conformance/checkout-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/checkout/refs/heads/main/llms/checkout-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/checkout-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/checkout/refs/heads/main/well-known/checkout-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/checkout-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/checkout/refs/heads/main/hosts/checkout-hosts.yml
  title: ''
  type: Hosts
  url: hosts/checkout-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/checkout/refs/heads/main/vendors/checkout-vendors.yml
  title: ''
  type: Vendors
  url: vendors/checkout-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/checkout/refs/heads/main/packages/checkout-packages.yml
  title: ''
  type: SDKs
  url: packages/checkout-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/checkout/refs/heads/main/packages/checkout-packages.yml
  title: ''
  type: Packages
  url: packages/checkout-packages.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.checkout.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.checkout.com/legal/terms-and-policies
- group: operate
  title: ''
  type: Support
  url: https://support.checkout.com
- group: operate
  title: ''
  type: StatusPage
  url: https://identity.checkout.com/app/statuspage_saml/exk1izzuix2ptvgqk0h8/sso/saml?SAMLRequest=fZLLbsIwEEV%2FJTuvnPfDWASJFlVFoioC2kU3yHUcYkHskHEQ5eubhFJoFyws2dK9Z%2B7MeAis3FV03JhCLcS%2BEWCsMYCojdTqUStoSlEvRX2QXLwtZikqjKmAOk7JFNsIGwwzDVTdVWoHoD0t0OFnJ7ImLVAq1tGuXpkJZaT5snkh%2BFY3xua6dFhVOVfcuueI49aTp1Mjj35lDpv91i3IbxVkPemaiz57inK2g7bgdJKidZKLgISej3MS%2BTgUCcHEHeQ49qIwicmAhTFppQCNmKq2pjIp8l0%2Fxp6LXbLyXBpFNAw%2BkDWvtdFc7x6kyqTapKipFdUMJFDFSgHUcLocv8yob7v08ywC%2BrxazfH8dblC1ruooW%2B%2BFSDrWO4U0C78fRK7rODWUt33VD9R0WjYqWnfXj26DJ2TjAwGcY4zPw9xyLiHSRb7mLOM5V4SBBn%2Fv86hcws6v%2F7%2BldE3&RelayState=https%3A%2F%2Fcheckout-services.statuspage.io%2F&SigAlg=http%3A%2F%2Fwww.w3.org%2F2001%2F04%2Fxmldsig-more%23rsa-sha256&Signature=bc0Uml1jiH3UR8BJDHFDVIDwkTg%2FUMkz1HyfQJZTSgjFUDb87cGZFo1HnSVjCjNyGnb7P756QWVdqy%2B5S3SSaAbVDOcaMPjm3dXbajeGe8EIb3CfyIEUdyOeoJ6caRoqTjo0zzsRIzOma4x6jYv6wJIwPGVGNJ1ZZ3uISuSoom4sGoYtBGbcQpYxsXdgFcDB6pqSl%2FVpgAoaZRjodT%2FlaeDPTFSNqXY4Z3lunCl0iKSkhEQ80epunGS9gWMPdv%2Bp%2F%2FFl6YdKHWV8vsN3Jgh0uZIfino1gE42Bt9tQDNasLU04pP7Yvr6nR4x%2Bpo9Kgm0b2Uee27rCRxpYaU9PVuvDQ%3D%3D
- group: start
  title: ''
  type: SignUp
  url: https://www.checkout.com/events/register-interest-padel
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.checkout.com/legal/privacy-notice
- group: commercial
  title: ''
  type: Pricing
  url: https://www.checkout.com/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://www.checkout.com/newsroom
- group: other
  title: ''
  type: Leadership
  url: https://www.checkout.com/leadership
- group: company
  title: ''
  type: Blog
  url: https://www.checkout.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://www.checkout.com/docs/card-issuing/card-program-setup
- group: docs
  title: ''
  type: Documentation
  url: https://docs.checkout.com/
- group: docs
  title: ''
  type: APIReference
  url: https://api-reference.checkout.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/checkout
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/checkout/refs/heads/main/security/checkout-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/checkout-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/checkout/refs/heads/main/security/checkout-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/checkout-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.checkout.com
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 403
    url: https://identity.checkout.com/mcp
  - status: 200
    url: https://www.checkout.com
  reason: partner-login
  state: gated
created: '2026-10-08'
description: Checkout is a global payments platform offering a suite of APIs and tools that enable businesses to accept, process, and manage online payments. It provides unified payments API, hosted payment pages, mobile SDKs, fraud detection, authentication, issuing, payouts, and advanced features like AI-driven intelligent acceptance and real‑time account updates. Checkout serves enterprises across e‑commerce, marketplaces, travel, gaming, fintech, and more, delivering high‑performance, secure, and scalable payment solutions worldwide.
image: https://cdn.prod.website-files.com/64db80a5e88c6b1723ff760b/67e2bd4ddf0a87a1400c020d_website-thumbnail.jpg
json_schemas:
- name: PostRequest
  property_count: 3
  slug: checkout-post-request
jsonld:
- class_count: 1
  name: Checkout Context
  property_count: 3
  slug: checkout-context
layout: provider
modified: '2026-10-08'
name: Checkout
nav: Providers
network: true
overview: 'Checkout is listed with 4 APIs on the [APIs.io](https://apis.io/) network, including Checkout API, Connect API, Payments API, and 1 more. Tagged areas include Payments, Fintech, E-Commerce, and Global.


  The Checkout catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Checkout''s developer surface includes authentication, support, signup flow, pricing, engineering blog, getting-started guide, documentation, and 24 more developer resources.'
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Checkout API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: checkout-rules
score:
  band: developing
  composite: 43.2
  coverage:
    artifact_dirs: 18
    catalog_earned: 46.2
    catalog_earned_first_party: 0.0
    catalog_gap: 68.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 22.0
    contract_quality: 25.4
    developer_ergonomics: 54.8
    discoverability: 64.3
    operational_transparency: 39.5
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 32.1
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Checkout Authentication
  slug: checkout-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Checkout Domain Security
  slug: checkout-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Checkout Vulnerability Disclosure
  slug: checkout-vulnerability-disclosure
  summary_line: Bugcrowd
slug: checkout
tags:
- Payments
- Fintech
- E-Commerce
- Global
website: https://www.checkout.com
---
