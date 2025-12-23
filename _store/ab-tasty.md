---
aid: ab-tasty
url: >-
  https://raw.githubusercontent.com/api-evangelist/ab-tasty/refs/heads/main/apis.yml
apis:
  - aid: ab-tasty:decision-api
    name: AB Tasty Decision API
    humanURL: https://docs.abtasty.com/server-side/decision-api/decision-api
    description: >-
      The AB Tasty Decision API is a server-side service that evaluates a
      visitors context against your active experiments, personalizations, and
      feature flags, then returns a deterministic decision: which campaigns the
      user qualifies for, the selected variation, and any variables or content
      to render. It centralizes targeting, traffic allocation, and bucketing so
      you can power A/B tests, gradual rollouts, and personalized experiences
      from backends, mobile apps, or edge workers while keeping user exposure
      consistent. You pass identifiers and attributes at request time, use the
      response to render the experience, and pair it with event tracking for
      measurement.
  - aid: ab-tasty:remote-control-api
    name: 'AB Tasty Remote Control API '
    humanURL: https://docs.abtasty.com/server-side/remote-control-api
    description: >-
      AB Tastys Remote Control API is a developer and QA tool that lets you
      programmatically drive the AB Tasty SDK from outside your app or page, so
      you can precisely control and observe experiments without changing
      production targeting. With it, you can preview or force specific campaigns
      and variations for a visitor, toggle or pause experiences, set
      visitor/context attributes, trigger goals and custom events, refresh
      decisions, and clear caches to reproduce clean states. Teams use it to
      debug implementation issues, run automated tests, and create deterministic
      scenarios for demos or CI pipelines, ensuring consistent, repeatable
      experiment behavior across environments.
name: AB Tasty
tags:
  - Unified
  - Aggregation
  - Experimentation
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
common:
  - url: https://www.abtasty.com/
    name: Website
    type: Website
    description: 'null'
  - url: https://www.abtasty.com/pricing/
    name: Pricing - abtasty
    type: Pricing
    description: 'null'
  - url: https://www.abtasty.com/resource-categories/case-studies/
    name: Case Studies
    type: CaseStudies
    description: 'null'
created: '2025-06-05'
modified: '2025-12-23'
position: Consuming
description: >-
  At AB Tasty, were your partner for pushing great ideas even further through
  optimization. We achieve this by empowering brands to build better experiences
  using personalization, experimentation, recommendations, merchandising, and
  the markets only emotions-based segmentation solution.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
specificationVersion: '0.19'

---