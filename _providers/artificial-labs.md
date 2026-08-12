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
    well_known_catalog: false
  schema_version: 0.2
  score: 9.0
  scored_at: '2026-08-11'
api_count: 0
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://artificial.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.artificial.io/docs-site/
- group: company
  title: ''
  type: About
  url: https://artificial.io/about/
- group: company
  title: ''
  type: Blog
  url: https://artificial.io/company/blog/
- group: operate
  title: ''
  type: Contact
  url: https://artificial.io/contact/
- group: operate
  title: ''
  type: Support
  url: https://artificial.io/contact/
- group: start
  title: ''
  type: Login
  url: https://docs.artificial.io/oauth2/start
- group: auth
  title: ''
  type: Security
  url: https://artificial.io/security/
- group: auth
  title: ''
  type: Compliance
  url: https://trust.artificial.io/
- group: auth
  title: ''
  type: TrustCenter
  url: security/artificial-labs-trust-center.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://artificial.io/website-terms/
- group: other
  title: ''
  type: EULA
  url: https://artificial.io/eula/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://artificial.io/privacy/
- group: company
  title: ''
  type: Careers
  url: https://artificial.io/careers/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/artificial-labs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/artificial-labs
- group: other
  title: ''
  type: OpenIDConnect
  url: https://auth.artificialos.com/.well-known/openid-configuration
- group: auth
  title: ''
  type: Authentication
  url: authentication/artificial-labs-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/artificial-labs-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/artificial-labs-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/artificial-labs-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/artificial-labs-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/artificial-labs-vulnerability-disclosure.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/artificial-labs-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/artificial-labs-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/artificial-labs-llms.txt
created: '2026-07-25'
description: 'Artificial Labs is a London-based insurance technology company building algorithmic and digital underwriting software for the specialty and reinsurance market, with the Lloyd''s of London subscription market as its home ground. Founded and headquartered in the City of London at 1-3 Frederick''s Place, and led by co-founders and co-CEOs David King and Johnny Bridges under chairman Martin Reith, the company sells three products to carriers, syndicates, MGAs and wholesale brokers: Smart Underwriting (a configurable lead-and-follow digital underwriting platform with appetite modelling and accept/refer/decline submission triage), Smart Placement (a broker-side placement and distribution platform) and Contract Builder (MRCv3-compliant structured digital contract creation, which powers PPL''s integrated Digital Contract Capability). Named customers and partners include Apollo, PPL, BMS Group, Lockton and McGill and Partners, and the firm is an alumnus of the Lloyd''s Lab accelerator.
  Its API posture is partner-gated and matches the London Market pattern: Artificial talks publicly and often about APIs as the connective tissue between broker PAS, carrier systems and its own platform, and describes real quote-and-bind flows in which risk data is pushed to the Artificial platform via API and a written line and rate are returned via API, but it publishes no public self-serve developer portal, no downloadable OpenAPI or Swagger definition, no public Postman collection and no public API host. api.artificial.io and developer.artificial.io do not resolve in DNS. The product documentation site at docs.artificial.io returns HTTP 200 on its landing page only, which states plainly "To view the documentation, you must sign in"; every product and reference path 302-redirects to an Auth0 authorization-code login at auth.artificialos.com, and docs robots.txt is Disallow all. Its GitHub organization, github.com/artificial-labs, exists but has zero public repositories. Where Artificial
  is genuinely and demonstrably standards-forward is ACORD: it joined the ACORD Solutions Group Licensed Integrator Partner program in October 2023, builds Contract Builder and Smart Placement on a structured data model incorporating MRCv3, ACORD GRLC and the Lloyd''s Core Data Record, validates contracts pre-submission against MRCv3 and ACORD standards, and consumes the ACORD Transcriber API for automated data extraction. That is the honest shape of this record: real, working, standards-aligned insurance APIs that are invisible from outside the contractual relationship.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-25'
name: Artificial Labs
nav: Providers
network: true
overview: 'Artificial Labs is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, United Kingdom, Insurtech, Underwriting, and Reinsurance.


  Artificial Labs'' developer surface includes documentation, engineering blog, support, authentication, and 22 more developer resources.'
random_paper: 3
scopes:
- name: Artificial Labs Scopes
  scope_count: 14
  slug: artificial-labs-scopes
  summary_line: 14 scopes · authorizationCode/clientCredentials
score:
  band: thin
  composite: 33.8
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 26.1
    discoverability: 68.5
    governance: 12.5
    operational_transparency: 15.8
  previous_composite: 33.8
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 80.3
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/artificial-labs/refs/heads/main/screenshots/artificial-labs-2026-07-25T201337.png
security:
- kind: authentication
  name: Artificial Labs Authentication
  slug: artificial-labs-authentication
  summary_line: oauth2/openIdConnect · 1 scheme
- kind: domain-security
  name: Artificial Labs Domain Security
  slug: artificial-labs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Artificial Labs Vulnerability Disclosure
  slug: artificial-labs-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Artificial Labs Trust Center
  slug: artificial-labs-trust-center
  summary_line: ISO 27001, Cyber Essentials Plus
slug: artificial-labs
tags:
- Insurance
- United Kingdom
- Insurtech
- Underwriting
- Reinsurance
- Specialty Insurance
- London Market
- Lloyd's of London
- Broker
- Policy Administration
- ACORD
- Algorithmic Underwriting
website: https://artificial.io/
---
