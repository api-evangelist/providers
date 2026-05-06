---
aid: sequoia-capital
name: Sequoia Capital
description: Sequoia Capital is one of the world's leading venture capital firms, founded in 1972 and headquartered in Menlo Park, California. Sequoia has backed transformative companies including Apple, Google, Oracle, Cisco, LinkedIn, Instagram, WhatsApp, YouTube, Airbnb, Stripe, and many others. Sequoia operates globally through dedicated funds including Sequoia Capital US/Europe, Sequoia India/Southeast Asia, and Sequoia China. This profile tracks Sequoia's developer resources, portfolio data APIs, and investment intelligence tools.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Venture Capital
  - Investment
  - Startup Funding
  - Private Equity
  - Portfolio Management
url: https://raw.githubusercontent.com/api-evangelist/sequoia-capital/refs/heads/main/apis.yml
created: '2026-05-02'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: sequoia-capital:sequoia-arc-api
    name: Sequoia Arc Program API
    description: Sequoia Arc is the firm's structured program for early-stage seed companies. The Arc program provides cohort-based resources, curriculum, and networking for seed-stage founders. Developer integrations connect Arc portfolio companies with Sequoia's operational resources.
    humanURL: https://www.sequoiacap.com/arc/
    tags:
      - Venture Capital
      - Seed Stage
      - Early Stage
      - Founder Resources
    properties:
      - type: Documentation
        url: https://www.sequoiacap.com/arc/
  - aid: sequoia-capital:crunchbase-api
    name: Crunchbase Investment Data API
    description: Crunchbase provides investment and startup data including Sequoia portfolio company information, funding rounds, valuations, and investor relationships. The Crunchbase API is widely used by analysts researching Sequoia's portfolio and deal history.
    humanURL: https://data.crunchbase.com/
    tags:
      - Venture Capital
      - Investment Data
      - Portfolio Research
      - Startup Data
    properties:
      - type: Documentation
        url: https://data.crunchbase.com/
      - type: Reference
        url: https://data.crunchbase.com/reference/get_data-entities-organizations
  - aid: sequoia-capital:pitchbook-api
    name: PitchBook Investment Data API
    description: PitchBook provides private equity and venture capital data including comprehensive Sequoia deal history, portfolio company valuations, fund performance, and limited partner information.
    humanURL: https://pitchbook.com/data/pitchbook-api
    tags:
      - Venture Capital
      - Investment Data
      - Private Markets
      - Fund Performance
    properties:
      - type: Documentation
        url: https://pitchbook.com/data/pitchbook-api
common:
  - type: Website
    url: https://www.sequoiacap.com/
  - type: Blog
    url: https://www.sequoiacap.com/articles/
  - type: GitHub
    url: https://github.com/sequoia-capital
  - type: Portfolio
    url: https://www.sequoiacap.com/companies/
  - type: ArcProgram
    url: https://www.sequoiacap.com/arc/
  - type: Podcast
    url: https://www.sequoiacap.com/podcast/
  - type: LinkedIn
    url: https://www.linkedin.com/company/sequoia-capital/
  - type: JSONSchema
    url: json-schema/sequoia-portfolio-company-schema.json
  - type: JSONStructure
    url: json-structure/sequoia-portfolio-company-structure.json
  - type: JSONLDContext
    url: json-ld/sequoia-context.jsonld
  - type: Examples
    url: examples/sequoia-portfolio-company-example.json
  - type: Vocabulary
    url: vocabulary/sequoia-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
