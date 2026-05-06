---
aid: thomson-reuters
name: Thomson Reuters
description: Thomson Reuters provides over 137 APIs across legal, tax and accounting, risk and fraud, and trade and supply industries through their global developer portal. APIs cover Westlaw legal research, Checkpoint tax content, ONESOURCE tax software, HighQ document management, Legal Tracker matter management, and risk and fraud solutions including identity verification and adverse media screening.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Legal
  - Tax
  - Finance
  - Risk
  - Fraud
  - Compliance
  - Data
created: '2026-03-16'
modified: '2026-05-03'
url: https://raw.githubusercontent.com/api-evangelist/thomson-reuters/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: thomson-reuters:westlaw-api
    name: Thomson Reuters Westlaw API
    description: Access Westlaw legal research content including case law, statutes, regulations, and secondary sources. Includes SEC Filings API, Dockets API, and Litigation Analytics providing structured legal data for integration into knowledge management and legal workflow systems.
    humanURL: https://developers.thomsonreuters.com/
    tags:
      - Legal
      - Research
      - Case Law
      - Litigation
      - Westlaw
    properties:
      - type: Documentation
        url: https://developers.thomsonreuters.com/
      - type: GitHubOrganization
        url: https://github.com/thomsonreuters
  - aid: thomson-reuters:checkpoint-api
    name: Thomson Reuters Checkpoint API
    description: Checkpoint Search API provides access to Thomson Reuters Checkpoint tax and accounting research content including tax regulations, guidance, and analytical tools for tax professionals and accountants.
    humanURL: https://developers.thomsonreuters.com/
    tags:
      - Tax
      - Accounting
      - Checkpoint
      - Research
    properties:
      - type: Documentation
        url: https://developers.thomsonreuters.com/
  - aid: thomson-reuters:onesource-api
    name: Thomson Reuters ONESOURCE API
    description: ONESOURCE APIs provide integration with Thomson Reuters tax compliance software including income tax, indirect tax, transfer pricing, and global trade management. Enables workflow automation for tax calculations, filings, and reporting.
    humanURL: https://developers.thomsonreuters.com/
    tags:
      - Tax
      - Compliance
      - ONESOURCE
      - Workflow
    properties:
      - type: Documentation
        url: https://developers.thomsonreuters.com/
  - aid: thomson-reuters:highq-api
    name: Thomson Reuters HighQ API
    description: HighQ APIs support document synchronization between HighQ and external document management systems, enabling integration with legal matter management, client collaboration, and document automation workflows.
    humanURL: https://developers.thomsonreuters.com/
    tags:
      - Legal
      - Document Management
      - HighQ
      - Collaboration
    properties:
      - type: Documentation
        url: https://developers.thomsonreuters.com/
  - aid: thomson-reuters:legal-tracker-api
    name: Thomson Reuters Legal Tracker API
    description: Legal Tracker API enables users to create and manage legal matters, invoices, budgets, and vendor relationships programmatically, supporting e-billing and legal spend management integrations.
    humanURL: https://developers.thomsonreuters.com/
    tags:
      - Legal
      - Matter Management
      - E-billing
      - Legal Tracker
    properties:
      - type: Documentation
        url: https://developers.thomsonreuters.com/
  - aid: thomson-reuters:risk-fraud-api
    name: Thomson Reuters Risk and Fraud API
    description: Risk and Fraud APIs automate customer onboarding, identity verification, risk assessments, adverse media screening, investigations, and compliance monitoring. Includes tools for KYC, AML, and third-party risk management.
    humanURL: https://developers.thomsonreuters.com/
    tags:
      - Risk
      - Fraud
      - KYC
      - AML
      - Identity Verification
      - Compliance
    properties:
      - type: Documentation
        url: https://developers.thomsonreuters.com/
common:
  - type: Website
    url: https://www.thomsonreuters.com/
  - type: Documentation
    url: https://developers.thomsonreuters.com/
  - type: DeveloperPortal
    url: https://developers.thomsonreuters.com/
  - type: GitHubOrganization
    url: https://github.com/thomsonreuters
  - type: Blog
    url: https://www.thomsonreuters.com/en/technology/technology-blog.html
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
