---
api_count: 1
apis:
- baseURL: https://api.aclid.bio
  baseurl_source: declared
  description: REST API for biosecurity screening and compliance automation. Initiate a pathogen/toxin sequence screen from a FASTA or FASTQ upload, a CSV of named sequences, or an inline JSON payload; poll or retri
  name: Aclid API
  slug: aclid-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aclid-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.aclid.bio/
- group: docs
  title: ''
  type: Documentation
  url: https://api.aclid.bio/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.aclid.bio/docs
- group: start
  title: ''
  type: Login
  url: https://dash.aclid.bio
- group: operate
  title: ''
  type: Support
  url: https://www.aclid.bio/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aclid.bio/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aclid.bio/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.aclid.bio
- group: auth
  title: ''
  type: Authentication
  url: authentication/aclid-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/aclid-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/aclid-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/aclid-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/aclid-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/aclid-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/aclid-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/aclid-components.yml
- group: build
  title: ''
  type: Packages
  url: packages/aclid-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/aclid-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/aclid-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aclid-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/aclid-openapi-overlay.yaml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/aclid-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/aclid-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/aclid-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://dash.aclid.bio/.well-known/security.txt
- group: start
  title: ''
  type: Sandbox
  url: sandbox/aclid-sandbox.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/aclid-compliance-reason-codes.yml
created: '2026-09-06'
description: Aclid is a biosecurity and biosafety compliance automation platform for the synthetic biology supply chain. Gene synthesis providers, biofoundries and research institutions use Aclid to screen DNA/RNA orders for pathogenic, toxic and export-controlled sequence elements, to verify the customers placing those orders against international sanctions and watchlists, and to run and document the compliance review that regulators and the OSTP Framework for Nucleic Acid Synthesis Screening expect. The platform is delivered as a hosted dashboard plus a public REST API (api.aclid.bio) that initiates screens from FASTA, FASTQ, CSV or inline sequence payloads, returns structured findings with per-framework regulatory reason codes (US Commerce Control List, EU Dual-Use, Australia Group and others), manages customers and verifications, and issues hosted or embeddable customer-verification flows. Founded 2021 in New York by Kevin Flyangolts with scientific founder Harris H. Wang of Columbia
  University.
image: https://cdn.prod.website-files.com/671c02ec6144c945bfc5aa9c/6727db79308f1e1139096dd3_Logo.svg
layout: provider
modified: '2026-09-06'
name: Aclid
nav: Providers
network: true
overview: 'Aclid publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Biosecurity, Biosafety, Compliance, Synthetic Biology, and Life Sciences.


  Aclid''s developer surface includes documentation, API reference, support, authentication, sandbox, and 24 more developer resources.'
plans:
- name: Aclid Plans Pricing
  plan_count: 0
  slug: aclid-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Aclid Rate Limits
  slug: aclid-rate-limits
security:
- kind: authentication
  name: Aclid Authentication
  slug: aclid-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Aclid Domain Security
  slug: aclid-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Aclid Vulnerability Disclosure
  slug: aclid-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: aclid
tags:
- Biosecurity
- Biosafety
- Compliance
- Synthetic Biology
- Life Sciences
- DNA Sequence Screening
- Sanctions Screening
- Export Control
- Biotechnology
- Risk Assessment
- Know Your Customer
website: https://www.aclid.bio/
---
