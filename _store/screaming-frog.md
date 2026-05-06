---
aid: screaming-frog
name: Screaming Frog
description: Screaming Frog is a UK-based SEO software company and search marketing agency, best known for the SEO Spider website crawler tool used by SEO professionals worldwide to perform technical SEO audits, crawl analysis, and integrations with third-party APIs. The SEO Spider integrates with Google Analytics (GA4), Google Search Console, PageSpeed Insights, Ahrefs, Majestic, Moz, OpenAI, Gemini, Ollama, and Anthropic. Screaming Frog also offers a free Log File Analyser for analyzing server log files to understand search bot behavior.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - SEO
  - Search Engine Optimization
  - Website Crawler
  - Technical Audit
  - Marketing
  - Analytics
created: '2026-05-02'
modified: '2026-05-02'
url: https://raw.githubusercontent.com/api-evangelist/screaming-frog/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: screaming-frog:seo-spider
    name: Screaming Frog SEO Spider
    description: The Screaming Frog SEO Spider is a desktop website crawler for Windows, macOS, and Ubuntu that performs comprehensive technical SEO audits. It crawls websites to find broken links, analyze page titles and meta data, discover duplicate content, generate XML sitemaps, and integrate with third-party APIs including Google Analytics, Google Search Console, PageSpeed Insights, Ahrefs, Majestic, Moz, and AI services (OpenAI, Gemini, Ollama, Anthropic). The Spider acts as an API consumer, pulling external metrics and data into crawl reports.
    humanURL: https://www.screamingfrog.co.uk/seo-spider/
    tags:
      - SEO
      - Crawler
      - Technical Audit
      - Analytics Integration
    properties:
      - type: Documentation
        url: https://www.screamingfrog.co.uk/seo-spider/user-guide/
      - type: Pricing
        url: https://www.screamingfrog.co.uk/seo-spider/pricing/
      - type: ReleaseHistory
        url: https://www.screamingfrog.co.uk/seo-spider/release-history/
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/screaming-frog/refs/heads/main/json-schema/screaming-frog-crawl-result-schema.json
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/screaming-frog/refs/heads/main/json-structure/screaming-frog-crawl-result-structure.json
      - type: JSONLDContext
        url: https://raw.githubusercontent.com/api-evangelist/screaming-frog/refs/heads/main/json-ld/screaming-frog-context.jsonld
      - type: Vocabulary
        url: https://raw.githubusercontent.com/api-evangelist/screaming-frog/refs/heads/main/vocabulary/screaming-frog-vocabulary.yml
      - type: Example
        url: https://raw.githubusercontent.com/api-evangelist/screaming-frog/refs/heads/main/examples/screaming-frog-crawl-result-example.json
  - aid: screaming-frog:log-file-analyser
    name: Screaming Frog Log File Analyser
    description: The Screaming Frog Log File Analyser is a free desktop tool that allows SEO professionals to upload and analyze server log files to understand how search bots are crawling a website. It identifies which pages bots visit, how frequently they crawl them, and highlights crawl budget inefficiencies. Available for Windows, macOS, and Ubuntu with a paid license removing crawl limits.
    humanURL: https://www.screamingfrog.co.uk/log-file-analyser/
    tags:
      - SEO
      - Log Analysis
      - Bot Detection
      - Crawl Analysis
      - Crawl Budget
    properties:
      - type: Documentation
        url: https://www.screamingfrog.co.uk/log-file-analyser/user-guide/
common:
  - type: Website
    url: https://www.screamingfrog.co.uk/
  - type: Blog
    url: https://www.screamingfrog.co.uk/blog/
  - type: Contact
    url: https://www.screamingfrog.co.uk/contact/
  - type: Pricing
    url: https://www.screamingfrog.co.uk/seo-spider/pricing/
  - type: Support
    url: https://www.screamingfrog.co.uk/seo-spider/faq/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
