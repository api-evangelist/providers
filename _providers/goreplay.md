---
access_model:
  confidence: high
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - pricing
  trial: false
  try_now: false
api_count: 1
apis:
- description: 'GoReplay captures live HTTP traffic with libpcap and replays it against a test target, letting teams validate deploys, configuration changes and infrastructure changes against real production traffic '
  name: GoReplay
  slug: goreplay-tool
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://goreplay.org
- group: docs
  title: ''
  type: Documentation
  url: https://goreplay.org/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://goreplay.org/docs/installation/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/probelabs/goreplay
- group: operate
  title: ''
  type: Support
  url: https://github.com/probelabs/goreplay/issues
- group: company
  title: ''
  type: Blog
  url: https://goreplay.org/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://goreplay.org/pro/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://github.com/probelabs/goreplay/blob/master/COMM-LICENSE
- group: build
  title: ''
  type: CLI
  url: cli/goreplay-cli.yml
- group: build
  title: ''
  type: Packages
  url: packages/goreplay-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/goreplay-llms.txt
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/goreplay-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/goreplay-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/goreplay-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/goreplay-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/goreplay-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/goreplay-rate-limits.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/goreplay-domain-security.yml
created: '2026-03-26'
description: GoReplay is an open source network traffic capture and replay tool, distributed as a single `gor` binary under LGPL-3.0, that records live HTTP traffic on a server and replays it against another environment for shadow testing, load testing with real production traffic, and debugging. It sits off the critical path rather than acting as a proxy, captures via libpcap without application changes, and can filter, rewrite or hand each message to external middleware before replay. A commercial GoReplay PRO edition ($2,950/year) adds Amazon S3 capture storage, binary protocol support, keep-alive TCP session recognition and dedicated support. GoReplay publishes no HTTP API of its own; its machine-readable contract is the CLI flag surface plus a documented middleware STDIN/STDOUT wire protocol.
finops:
- name: Goreplay Finops
  service_category: API
  slug: goreplay-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/goreplay.png
layout: provider
modified: '2026-09-13'
name: GoReplay
nav: Providers
network: true
overview: 'GoReplay publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include API Testing, Developer Tools, HTTP Traffic, Load Testing, and Network Capture.


  GoReplay''s developer surface includes documentation, getting-started guide, support, engineering blog, pricing, CLI, changelog, and 11 more developer resources.'
plans:
- name: Goreplay Plans Pricing
  plan_count: 2
  slug: goreplay-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Goreplay Rate Limits
  slug: goreplay-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/goreplay/refs/heads/main/screenshots/goreplay-2026-06-20T182250.png
security:
- kind: domain-security
  name: Goreplay Domain Security
  slug: goreplay-domain-security
  summary_line: TLSv1.3 · HSTS
slug: goreplay
tags:
- API Testing
- Developer Tools
- HTTP Traffic
- Load Testing
- Network Capture
- Open-Source
- Traffic Replay
website: https://goreplay.org
---
