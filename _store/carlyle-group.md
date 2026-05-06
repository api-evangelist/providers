---
aid: carlyle-group
url: https://raw.githubusercontent.com/api-evangelist/carlyle-group/refs/heads/main/apis.yml
name: The Carlyle Group
description: 'The Carlyle Group (NASDAQ: CG) is a global investment firm that deploys private capital across Global Private Equity, Global Credit, Global Investment Solutions (AlpInvest), and carveouts such as Carlyle Direct Lending. Carlyle does not publish a public developer API. Institutional LPs, co-investors, and portfolio companies interact with the firm through a set of private, authentication-gated portals: LP Connect for fund investors, Carlyle Direct Lending''s portal for direct lending clients, the Carlyle Global Portfolio Solutions (resources.carlyle.com) portal, and brand experiences such as Carlyle & Co. Integrations with fund administrators, custodians, and placement agents run through bespoke secure file exchange and vendor-managed APIs.'
type: Index
x-type: company
position: Consumer
access: Partner
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Alternative Assets
  - Asset Management
  - Direct Lending
  - Global Credit
  - Investment Firm
  - Investor Portal
  - Limited Partners
  - Private Credit
  - Private Equity
  - Real Assets
created: '2026-03-23'
modified: '2026-04-23'
specificationVersion: '0.19'
apis:
  - aid: carlyle-group:lp-connect
    name: Carlyle LP Connect Portal
    description: LP Connect is Carlyle's secure portal for Limited Partners and their advisors to access fund reporting, capital calls and distributions, investor statements, tax documents, and ad-hoc diligence materials. Access is provisioned by Carlyle on request. There is no public API; the portal is a web application with email-based credential recovery.
    humanURL: https://lpconnect.carlyle.com
    tags:
      - Investor Portal
      - Limited Partners
      - Private Equity
    properties:
      - url: https://lpconnect.carlyle.com
        type: Portal
      - url: https://lpconnect.carlyle.com/login.jsp
        type: Login
    x-features:
      - LP fund reporting and capital activity
      - Capital call and distribution notices
      - Tax documents (K-1s, PFIC) and investor statements
      - Ad-hoc diligence and side letter documents
      - Email-based credential recovery
    x-use-cases:
      - Family office LP operations
      - Pension and endowment staff reporting
      - Fund-of-funds due diligence workflows
      - Third-party LP administration
  - aid: carlyle-group:direct-lending-portal
    name: Carlyle Direct Lending Investor Portal
    description: Carlyle Direct Lending operates a dedicated investor portal for clients of Carlyle's direct lending funds and BDC vehicles. The portal supports modern web browsers and is used for reporting, distributions, and investor communications.
    humanURL: https://directlending.carlyle.com
    tags:
      - BDC
      - Direct Lending
      - Investor Portal
      - Private Credit
    properties:
      - url: https://directlending.carlyle.com
        type: Portal
    x-features:
      - BDC and direct lending fund reporting
      - Distribution and capital activity notices
      - Modern browser support (Chrome, Edge, Safari, Firefox, Opera)
    x-use-cases:
      - BDC shareholder account access
      - Institutional direct lending LP reporting
      - RIA/advisor portfolio oversight
  - aid: carlyle-group:global-portfolio-solutions
    name: Carlyle Global Portfolio Solutions Portal
    description: The Carlyle Global Portfolio Solutions Portal (resources.carlyle.com) is the secure workspace used by Carlyle's portfolio operations team, portfolio company executives, and advisors to share tools, templates, and operational playbooks across the portfolio.
    humanURL: https://resources.carlyle.com/carlyle/login
    tags:
      - Portfolio Operations
      - Portfolio Solutions
      - Private Equity
    properties:
      - url: https://resources.carlyle.com/carlyle/login
        type: Portal
    x-features:
      - Portfolio operations resources and templates
      - Executive community and tooling
      - Secure document sharing
    x-use-cases:
      - Portco finance and HR standardization
      - Value-creation playbook distribution
      - M&A and carve-out support
common:
  - type: Website
    url: https://www.carlyle.com/
  - type: Investor Relations
    url: https://ir.carlyle.com/
  - type: Public Investors
    url: https://ir.carlyle.com/
  - type: LP Connect
    url: https://lpconnect.carlyle.com
  - type: Direct Lending Portal
    url: https://directlending.carlyle.com
  - type: Global Portfolio Solutions Portal
    url: https://resources.carlyle.com/carlyle/login
  - type: AlpInvest
    url: https://www.carlylealpinvest.com/
  - type: Login
    url: https://www.carlyle.com/user/login
  - type: About
    url: https://www.carlyle.com/about-carlyle
  - type: Careers
    url: https://www.carlyle.com/careers
  - type: Contact
    url: https://www.carlyle.com/contact-us
  - type: Privacy Policy
    url: https://www.carlyle.com/privacy-policy
  - type: Terms of Service
    url: https://www.carlyle.com/terms-of-use
  - type: LinkedIn
    url: https://www.linkedin.com/company/the-carlyle-group
  - type: X
    url: https://x.com/OneCarlyle
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
