---
aid: symetra-financial
url: https://raw.githubusercontent.com/api-evangelist/symetra-financial/refs/heads/main/apis.yml
name: Symetra Financial
description: Symetra Financial Corporation is a diversified financial services company headquartered in Bellevue, Washington, providing employee benefits, annuities, and life insurance products to individuals, families, and businesses through independent advisors and financial institutions. A subsidiary of Sumitomo Life Insurance Company since 2016, Symetra offers medical stop-loss insurance, group life and disability income protection, supplemental health coverage, fixed and indexed annuities, registered index-linked annuities, income annuities, term life, and permanent life insurance. The company offers API and EDI-based data integrations for benefits administrators and HR platforms.
image: https://www.symetra.com/favicon.ico
tags:
  - Annuities
  - Benefits
  - Employee Benefits
  - Financial Services
  - Insurance
  - Life Insurance
  - Stop Loss
created: '2026-05-03'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: symetra-financial:symetra-benefits-api
    name: Symetra Benefits Administration API
    description: Symetra's Benefits Administration API enables HR platforms, benefits administrators, and technology partners to integrate with Symetra's group benefits products. The API supports automated data exchange for enrollment, eligibility, claims, short-term disability, absence management, and stop-loss insurance. It provides single sign-on (SSO) connectivity for evidence of insurability (EOI) and automated decision status updates, integrating with platforms such as Workday.
    humanURL: https://www.symetra.com/learn/articles-for-employers/technology-solutions/
    baseURL: https://api.symetra.com
    tags:
      - Benefits Administration
      - Claims
      - EDI
      - Eligibility
      - Employee Benefits
      - Enrollment
      - HR Integration
      - Insurance
      - Stop Loss
    properties:
      - type: Documentation
        url: https://www.symetra.com/learn/articles-for-employers/technology-solutions/
      - type: Website
        url: https://www.symetra.com/for-employers/
  - aid: symetra-financial:symetra-annuities-api
    name: Symetra Annuities API
    description: API for accessing Symetra annuity product information, rates, and illustrations. Supports fixed deferred annuities, fixed indexed annuities, registered index-linked annuities (RILA), and income annuities. Used by financial institutions and independent advisors to generate product illustrations, submit new business, and manage in-force contracts.
    humanURL: https://www.symetra.com/annuities/
    baseURL: https://api.symetra.com
    tags:
      - Annuities
      - Financial Advisors
      - Financial Services
      - Fixed Annuities
      - Income Annuities
      - Indexed Annuities
      - Insurance
      - RILA
      - Retirement
    properties:
      - type: Documentation
        url: https://www.symetra.com/annuities/
      - type: Website
        url: https://www.symetra.com/annuities/
  - aid: symetra-financial:symetra-life-insurance-api
    name: Symetra Life Insurance API
    description: API supporting Symetra's life insurance products including term life, SwiftTerm (instant-issue life insurance), and permanent life insurance. Enables financial advisors and distribution partners to access product information, request quotes, submit applications, track underwriting decisions, and manage in-force policies.
    humanURL: https://www.symetra.com/life-insurance/
    baseURL: https://api.symetra.com
    tags:
      - Financial Advisors
      - Insurance
      - Life Insurance
      - Permanent Life
      - Policy Management
      - Term Life
      - Underwriting
    properties:
      - type: Documentation
        url: https://www.symetra.com/life-insurance/
      - type: Website
        url: https://www.symetra.com/life-insurance/
common:
  - type: Website
    url: https://www.symetra.com
  - type: Login
    url: https://accounts.symetra.com/ui/login
  - type: Contact
    url: https://www.symetra.com/contact-us/
  - type: Privacy Policy
    url: https://www.symetra.com/privacy-policy/
  - type: Help Center
    url: https://www.symetra.com/help-center/
  - type: Blog
    url: https://www.symetra.com/benefits-blog-posts/
  - type: Technology Solutions
    url: https://www.symetra.com/learn/articles-for-employers/technology-solutions/
  - type: For Employers
    url: https://www.symetra.com/for-employers/
  - type: For Brokers
    url: https://www.symetra.com/for-brokers/
maintainers:
  - FN: API Evangelist
    email: info@apievangelist.com
---
