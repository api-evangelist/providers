---
api_count: 2
apis:
- baseURL: https://api.dips.no/dips.oauth
  baseurl_source: declared
  description: DIPS Federation Service (DFS) is the OpenID Connect provider and OAuth 2.0 authorization server in front of every Open DIPS API. Built on IdentityServer4 and certified by the OpenID Foundation, it sup
  name: DIPS Federation Service
  slug: dips-federation-service
- description: The DIPS HL7 FHIR R4 API exposes core clinical and administrative data from the DIPS Arena EHR — Patient, Person, RelatedPerson, Practitioner, PractitionerRole, Organization, Location, HealthcareServi
  name: DIPS FHIR R4 API
  slug: dips-fhir-r4-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dips-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.dips.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dips.developer.azure-api.net/
- group: docs
  title: ''
  type: Documentation
  url: https://dips.developer.azure-api.net/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://dips.developer.azure-api.net/apis
- group: start
  title: ''
  type: GettingStarted
  url: https://dips.developer.azure-api.net/getting-started
- group: start
  title: ''
  type: SignUp
  url: https://dips.developer.azure-api.net/signup
- group: start
  title: ''
  type: Login
  url: https://dips.developer.azure-api.net/signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dips.developer.azure-api.net/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dips.com/personvern
- group: operate
  title: ''
  type: Support
  url: https://www.dips.com/kontakt
- group: company
  title: ''
  type: Blog
  url: https://www.dips.com/innsikt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/DIPSAS
- group: company
  title: ''
  type: Partners
  url: https://dips.developer.azure-api.net/partner
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/dips-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/dips-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/dips-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/dips-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/dips-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/dips-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/dips-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dips-rate-limits.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/dips-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/dips-conformance.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/dips-data-model.yml
created: '2026-09-02'
description: DIPS AS is Norway's largest supplier of electronic health record (EHR) systems to hospitals, in operation since 1987 and headquartered in Bodø. Its DIPS Arena EHR is built on the openEHR reference model and exposes standardised HL7 FHIR R4 and openEHR REST interfaces. Through Open DIPS — a public developer portal and synthetic-data sandbox at dips.developer.azure-api.net — DIPS publishes an OpenID Connect provider (DIPS Federation Service), a FHIR Patient API and a SMART on FHIR launch surface, backed by a public FHIR R4 Implementation Guide and an openEHR archetype repository on GitHub.
image: https://dips.developer.azure-api.net/content/Dips_symbol.png
layout: provider
modified: '2026-09-02'
name: DIPS
nav: Providers
network: true
overview: 'DIPS publishes 1 API on the [APIs.io](https://apis.io/) network: Federation Service. Tagged areas include Company, Healthcare, Electronic Health Records, Health IT, and FHIR.


  DIPS''s developer surface includes documentation, API reference, getting-started guide, signup flow, support, engineering blog, sandbox, and 19 more developer resources.'
plans:
- name: Dips Plans Pricing
  plan_count: 1
  slug: dips-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Dips Rate Limits
  slug: dips-rate-limits
scopes:
- name: Dips Scopes
  scope_count: 0
  slug: dips-scopes
  summary_line: OAuth 2.0 · no documented scopes
security:
- kind: authentication
  name: Dips Authentication
  slug: dips-authentication
  summary_line: apiKey/openIdConnect · 3 schemes
- kind: domain-security
  name: Dips Domain Security
  slug: dips-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: dips
tags:
- Company
- Healthcare
- Electronic Health Records
- Health IT
- FHIR
- openEHR
- Interoperability
- Identity
- OpenID Connect
- Norway
- Hospitals
- SMART on FHIR
website: https://www.dips.com/
---
