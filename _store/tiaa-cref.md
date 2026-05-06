---
aid: tiaa-cref
name: TIAA-CREF
description: TIAA (Teachers Insurance and Annuity Association of America, formerly TIAA-CREF) is a Fortune 100 leading provider of financial services for people in the academic, research, medical, cultural, and government fields. With $1.5 trillion in assets under management, TIAA serves over 4.7 million individual customers and more than 12,000 institutional clients. Founded in 1918, TIAA invented the variable annuity in 1952 via the College Retirement Equities Fund (CREF) and is known for its TIAA Traditional fixed annuity and lifetime income solutions. TIAA wholly owns Nuveen Investments, a major institutional asset management firm. TIAA serves primarily non-profit organizations, universities, hospitals, and government entities with retirement plans including 403(b), 457(b), and 401(k) plans.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - 403b
  - Annuities
  - Asset Management
  - Fortune 100
  - Higher Education
  - Institutional
  - Insurance
  - Investments
  - Non Profit
  - Nuveen
  - Retirement
  - TIAA
url: https://raw.githubusercontent.com/api-evangelist/tiaa-cref/refs/heads/main/apis.yml
created: '2026-03-24'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: tiaa-cref:tiaa-retirement-plans
    name: TIAA Retirement Plans
    description: TIAA's retirement plan services for individual participants, covering 403(b), 457(b), 401(k), and IRA accounts. Products include TIAA Traditional fixed annuity, CREF variable annuities (stock, bond, money market, social choice, global equities, inflation-linked bond, equity index accounts), mutual funds, and the Brokerage Window for self-directed investing. TIAA RetirePlus provides custom target-date strategies with embedded lifetime income for institutional clients.
    humanURL: https://www.tiaa.org/public
    baseURL: https://www.tiaa.org/
    tags:
      - 403b
      - 457b
      - Annuities
      - CREF
      - IRA
      - Mutual Funds
      - Retirement
      - TIAA
    properties:
      - type: Website
        url: https://www.tiaa.org/public
      - type: Login
        url: https://auth.tiaa.org/public/authentication/login
      - type: Plan Sponsors
        url: https://www.tiaa.org/public/plansponsors
      - type: Investment Products
        url: https://www.tiaa.org/public/invest/services/wealth-management/investment-products
      - type: Lifetime Income
        url: https://www.tiaa.org/public/plansponsors/lifetime-income-leader
    contact:
      - FN: TIAA Customer Support
        url: https://www.tiaa.org/public/about-tiaa/contact
  - aid: tiaa-cref:tiaa-annuities
    name: TIAA Annuities
    description: TIAA's flagship annuity products for retirement income, including TIAA Traditional (a participating fixed annuity with guaranteed minimum plus historical above-floor credits), CREF variable annuities across multiple investment accounts, and the new TIAA MyChoice MYGA (a flexible-premium multi-year guaranteed annuity). TIAA is rated A++ by AM Best. Portfolios with TIAA Traditional have outperformed in over 90% of retirement scenarios per major studies.
    humanURL: https://www.tiaa.org/public
    tags:
      - Annuities
      - Fixed Annuity
      - Insurance
      - Lifetime Income
      - Retirement Income
      - Variable Annuity
    properties:
      - type: Documentation
        url: https://www.tiaa.org/public/pdf/t/tiaa-retirement-product-primer.pdf
  - aid: tiaa-cref:nuveen-investments
    name: Nuveen Investments
    description: Nuveen is TIAA's wholly owned institutional asset management subsidiary with $1.5 trillion AUM (as of March 2026). Nuveen provides mutual funds, ETFs, closed-end funds, target-date series with embedded lifetime income (Nuveen Lifecycle Income), responsible investing ESG strategies, fixed income, real assets, and alternatives. Nuveen collaborates with Morningstar Retirement, Transamerica, and other partners to distribute TIAA Secure Income Account solutions.
    humanURL: https://www.nuveen.com/
    baseURL: https://www.nuveen.com/
    tags:
      - Asset Management
      - ETFs
      - Fixed Income
      - Institutional
      - Mutual Funds
      - Nuveen
      - Target Date
    properties:
      - type: Website
        url: https://www.nuveen.com/
      - type: Documentation
        url: https://www.nuveen.com/en-us
  - aid: tiaa-cref:tiaa-wealth-management
    name: TIAA Wealth Management
    description: TIAA's wealth management services for individuals, including managed accounts, brokerage services, financial advisory services, life insurance, educational savings (529 plans), and banking products.
    humanURL: https://www.tiaa.org/public/invest/services/wealth-management
    tags:
      - Banking
      - Brokerage
      - Financial Advice
      - Insurance
      - Investments
      - Wealth Management
    properties:
      - type: Documentation
        url: https://www.tiaa.org/public/invest/services/wealth-management
common:
  - type: Website
    url: https://www.tiaa.org/public
  - type: About
    url: https://www.tiaa.org/public/about-tiaa
  - type: Plan Sponsors
    url: https://www.tiaa.org/public/plansponsors
  - type: Individual Investors
    url: https://www.tiaa.org/public
  - type: Login
    url: https://auth.tiaa.org/public/authentication/login
  - type: Nuveen
    url: https://www.nuveen.com/
  - type: Annual Report
    url: https://www.tiaa.org/public/about-tiaa/corporate-governance
  - type: Wikipedia
    url: https://en.wikipedia.org/wiki/TIAA
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/tiaa-cref/refs/heads/main/json-schema/tiaa-cref-retirement-account-schema.json
  - type: JSONStructure
    url: https://raw.githubusercontent.com/api-evangelist/tiaa-cref/refs/heads/main/json-structure/tiaa-cref-retirement-account-structure.json
  - type: JSONLDContext
    url: https://raw.githubusercontent.com/api-evangelist/tiaa-cref/refs/heads/main/json-ld/tiaa-cref-context.jsonld
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/tiaa-cref/refs/heads/main/vocabulary/tiaa-cref-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
