---
api_count: 0
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.graphitehealth.io/
- group: operate
  title: ''
  type: Support
  url: https://www.graphitehealth.io/contact
- group: company
  title: ''
  type: Blog
  url: https://www.graphitehealth.io/news
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/graphitehealth
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.graphitehealth.io/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.graphitehealth.io/privacy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/graphite-health/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/graphite_health
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/graphitehealth-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/graphitehealth-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/graphitehealth-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/graphitehealth-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/graphitehealth-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/graphitehealth-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/graphitehealth-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/graphitehealth-trust-center.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/graphitehealth-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/graphitehealth-rate-limits.yml
coverage:
  checked: '2026-09-02'
  detail: Graphite Health markets developer APIs, an SDK and a data sandbox on /platform and /marketplace, but /developers is a 308 redirect to that marketing page whose only call to action is a contact form — and the three API-shaped hosts that do exist in DNS (fhir.graphitehealth.io, labs-core.graphitehealth.io, id.graphitehealth.io) all refuse TCP 443 from the public internet, so the platform is reachable only from inside member health-system networks.
  evidence:
  - status: 308
    url: https://www.graphitehealth.io/developers
  - status: 200
    url: https://www.graphitehealth.io/marketplace
  - status: 0
    url: https://fhir.graphitehealth.io/metadata
  - status: 404
    url: https://www.graphitehealth.io/.well-known/api-catalog
  reason: sales-gate
  state: gated
created: '2026-09-02'
description: Graphite Health is a member-led, non-profit 501(c)(4) health-data infrastructure company founded by Intermountain Health, Presbyterian Healthcare Services and SSM Health, later joined by Kaiser Permanente and Emory Healthcare. It operates a platform that ingests, standardizes and integrates clinical data across member health systems — a connector library for clinical and external systems, a single interoperable data model, managed container runtimes, developer APIs and a data sandbox — and governs the S2 standard, an information standard encoding the operational semantics of health data whose adoption is funded by Gates Ventures. On top of the platform it runs an application marketplace whose apps must be certified under Graphite's Digital Hippocratic Oath. As of this profiling pass Graphite publishes no public developer documentation and no machine-readable contract; its FHIR, platform-core and identity hosts exist in DNS but refuse connections from the public internet.
image: https://www.graphitehealth.io/img/logo-alt.svg
layout: provider
modified: '2026-09-02'
name: Graphite Health
nav: Providers
network: true
overview: 'Graphite Health is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Health Data, Interoperability, and Clinical Data.


  Graphite Health''s developer surface includes support, engineering blog, and 16 more developer resources.'
plans:
- name: Graphitehealth Plans Pricing
  plan_count: 0
  slug: graphitehealth-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Graphitehealth Rate Limits
  slug: graphitehealth-rate-limits
security:
- kind: domain-security
  name: Graphitehealth Domain Security
  slug: graphitehealth-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Graphitehealth Vulnerability Disclosure
  slug: graphitehealth-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Graphitehealth Trust Center
  slug: graphitehealth-trust-center
  summary_line: SSAE 18 SOC 2 Type 1, SSAE 18 SOC 2 Type 2
slug: graphitehealth
tags:
- Company
- Healthcare
- Health Data
- Interoperability
- Clinical Data
- FHIR
- openEHR
- Data Standards
- Marketplace
- Non-Profit
- Digital Health
website: https://www.graphitehealth.io/
---
