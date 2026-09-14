---
access_model:
  confidence: medium
  label: Anonymous, keyless read access. GET https://hpsf.io/wp-json/tribe/events/v1/events returns 200 with no credential. Writes require WordPress Application Passwords, which are not offered to the public.
  onboarding: unknown
  pricing: free
  public: true
  source:
  - https://hpsf.io/wp-json/tribe/events/v1/events
  trial: false
  try_now: true
api_count: 2
apis:
- baseURL: https://hpsf.io/wp-json/tribe/events/v1
  baseurl_source: declared
  description: The stable Events Calendar v1 REST API on hpsf.io, serving HPSF's conference and event calendar as JSON - HPSFcon, SC and CppCon listings with start and end dates, timezone details, cost, website, fea
  name: HPSF Events API
  slug: hpsf-events-api
- baseURL: https://hpsf.io/wp-json/tec/v1
  baseurl_source: declared
  description: The newer Events Calendar tec/v1 REST API on hpsf.io - an OpenAPI 3.0.4 contract with 17 operations over events, venues, organizers and recurring series, with named operationIds, declared BasicAuth an
  name: HPSF Events Calendar TEC v1 API
  slug: hpsf-tec-events-api
- description: The WordPress REST route index at https://hpsf.io/wp-json/ - the anchor the site's RFC 9727 /.well-known/api-catalog linkset points at. It returns the site identity, the 15 registered namespaces, 99 r
  name: HPSF Site Discovery API
  slug: hpsf-site-discovery-api
artifact_total: 8
asyncapis:
- description: ''
  name: Hpsf Event Surface
  slug: hpsf-event-surface
common:
- group: company
  title: ''
  type: Website
  url: https://www.hpsf.io/
- group: company
  title: ''
  type: About
  url: https://hpsf.io/about/
- group: docs
  title: ''
  type: Documentation
  url: https://hpsf.io/projects/
- group: docs
  title: ''
  type: APIReference
  url: https://hpsf.io/wp-json/tribe/events/v1/doc
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hpsfoundation
- group: company
  title: ''
  type: Blog
  url: https://hpsf.io/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://hpsf.io/feed/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/HPSF
- group: company
  title: ''
  type: Bluesky
  url: https://bsky.app/profile/hpsf.bsky.social
- group: operate
  title: ''
  type: Slack
  url: https://join.slack.com/t/hpsf/shared_invite/zt-3p95c8ety-_IW77jGKG35KgmFDGuDbsg
- group: operate
  title: ''
  type: Support
  url: https://helpcenter.linuxfoundation.org/en/
- group: operate
  title: ''
  type: Contact
  url: https://hpsf.io/contact/
- group: start
  title: ''
  type: SignUp
  url: https://enrollment.lfx.linuxfoundation.org/?project=hpsf
- group: commercial
  title: ''
  type: Pricing
  url: https://hpsf.io/join/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.linuxfoundation.org/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.linuxfoundation.org/legal/privacy-policy
- group: other
  title: ''
  type: Charter
  url: https://github.com/hpsfoundation/foundation/blob/main/charter.md
- group: other
  title: ''
  type: Governance
  url: https://hpsf.io/tac/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/hpsf-well-known.yml
- group: other
  title: ''
  type: ContentSignal
  url: https://hpsf.io/robots.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hpsf-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/hpsf-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/hpsf-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/hpsf-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/hpsf-lifecycle.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/hpsf-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/hpsf-data-model.yml
- group: build
  title: ''
  type: Examples
  url: examples/hpsf-examples.yml
- group: build
  title: ''
  type: Packages
  url: packages/hpsf-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/hpsf-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hpsf-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hpsf-domain-security.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/hpsf-mcp.yml
created: '2026-03-16'
description: 'The High Performance Software Foundation (HPSF) is a Linux Foundation project and neutral hub for open source high performance computing software, founded in 2024 and governed by a Governing Board, a Technical Advisory Council (TAC) and an Outreach Committee. HPSF hosts and supports a portable core software stack for HPC - including Spack, Kokkos, Apptainer, E4S, HPX, Charliecloud, Chapel, Viskores, Flux Framework and Wi4MPI - across Core, Established and Emerging project stages, and runs HPSFcon alongside a presence at SC and CppCon. Organizations join at Premier, General or Associate tier; projects apply to the TAC. HPSF publishes no developer program and ships no SDKs, but hpsf.io is a machine-readable surface in its own right: it serves an RFC 9727 /.well-known/api-catalog linkset, an llms.txt, a Content-Signal AI usage preference in robots.txt, and two live OpenAPI documents describing a publicly callable events API covering HPSF conferences, venues, organizers and event
  taxonomies. The WordPress wp/v2 content routes are advertised in the namespace list but are disabled on this installation.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hpsf.png
layout: provider
modified: '2026-09-13'
name: High Performance Software Foundation
nav: Providers
network: true
overview: 'High Performance Software Foundation publishes 2 APIs on the [APIs.io](https://apis.io/) network: HPSF Events API and HPSF Events Calendar TEC v1 API. Tagged areas include HPC, Linux Foundation, Open-Source, Scientific Computing, and Foundation.


  The High Performance Software Foundation catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  High Performance Software Foundation''s developer surface includes documentation, API reference, engineering blog, support, signup flow, pricing, authentication, and 27 more developer resources.'
plans:
- name: Hpsf Plans Pricing
  plan_count: 0
  slug: hpsf-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Hpsf Rate Limits
  slug: hpsf-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/hpsf/refs/heads/main/screenshots/hpsf-2026-06-20T182854.png
security:
- kind: authentication
  name: Hpsf Authentication
  slug: hpsf-authentication
  summary_line: none/http · 2 schemes
- kind: domain-security
  name: Hpsf Domain Security
  slug: hpsf-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hpsf
tags:
- HPC
- Linux Foundation
- Open-Source
- Scientific Computing
- Foundation
- Supercomputing
- Open-Governance
- Events
- Conferences
- Research-Computing
- Nonprofit
- Content
website: https://www.hpsf.io/
---
