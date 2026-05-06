---
aid: aarons
url: https://raw.githubusercontent.com/api-evangelist/aarons/refs/heads/main/apis.yml
name: Aaron's
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Lease-to-Own
  - Retail
  - Furniture
  - Electronics
  - Appliances
  - Consumer Finance
description: Aaron's is a lease-to-own retailer of furniture, consumer electronics, home appliances, and accessories serving customers across the United States and Canada. They provide flexible payment options including rent-to-own leasing with instant approval, online account management, and EZPay automatic payments.
created: '2026-04-19'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: aarons:aarons-lease-application
    name: Aaron's Lease Application
    tags:
      - Lease-to-Own
      - Consumer Finance
      - Credit
      - Applications
    humanURL: https://www.aarons.com/apply
    properties:
      - url: https://www.aarons.com/apply
        type: Documentation
    description: Aaron's online lease application and approval system enabling customers to apply for lease-to-own financing before shopping. Provides instant approval decisions and leasing power discovery for furniture, electronics, and appliances.
  - aid: aarons:aarons-account-management
    name: Aaron's Account Management
    tags:
      - Account Management
      - Payments
      - Lease Management
    humanURL: https://www.aarons.com
    properties:
      - url: https://www.aarons.com
        type: Documentation
    description: Aaron's online account management portal for customers to manage their lease accounts, make payments, set up EZPay automatic payments, track orders, and manage lease and payment information.
  - aid: aarons:aarons-product-catalog
    name: Aaron's Product Catalog
    tags:
      - Retail
      - Furniture
      - Electronics
      - Appliances
      - Lease-to-Own
    humanURL: https://www.aarons.com
    properties:
      - url: https://www.aarons.com
        type: Documentation
    description: Aaron's lease-to-own product catalog covering furniture (bedroom, living room, dining), electronics (TVs, laptops, gaming), and appliances (washers, dryers, refrigerators) from top brands including Ashley Furniture, Samsung, Sony, and GE. Includes clearance and previously leased inventory.
common:
  - type: Website
    url: https://www.aarons.com
  - type: Login
    url: https://www.aarons.com/account/login
  - type: SignUp
    url: https://www.aarons.com/apply
  - type: Features
    data:
      - name: Instant Lease Approval
        description: Online lease application with instant approval for customers to discover their leasing power before shopping in-store or online.
      - name: EZPay Automatic Payments
        description: Automatic payment setup (EZPay) for convenient, scheduled lease payment processing without manual intervention.
      - name: Online Payment Processing
        description: Online payment portal for customers to make one-time or recurring lease payments through the Aaron's website.
      - name: Express Delivery
        description: Express delivery in 2-3 days for eligible products to customer homes, with professional installation and setup.
      - name: Store Locator
        description: Store locator to find nearby Aaron's locations for in-store shopping, pickup, and customer service.
      - name: Account Management Portal
        description: Online account portal for tracking orders, managing lease details, viewing payment history, and saving favorite products.
      - name: Previously Leased Inventory
        description: Clearance and previously leased product inventory available at reduced lease rates for budget-conscious customers.
  - type: UseCases
    data:
      - name: Furniture Lease-to-Own
        description: Customers acquiring bedroom sets, sofas, sectionals, and dining furniture through flexible lease-to-own payment plans.
      - name: Electronics Access
        description: Consumers accessing TVs, laptops, gaming consoles, and audio equipment through affordable weekly or monthly lease payments.
      - name: Appliance Leasing
        description: Households obtaining washers, dryers, refrigerators, and ranges through lease-to-own options with delivery and installation.
      - name: Credit-Challenged Consumer Financing
        description: Consumers with limited or poor credit history accessing household goods through Aaron's flexible lease-to-own programs.
      - name: Temporary Furnishing
        description: Short-term furniture and appliance needs for relocating individuals or temporary housing situations via lease agreements.
  - type: Integrations
    data:
      - name: Progressive Leasing
        description: Aaron's Holdings subsidiary Progressive Leasing provides embedded lease-to-own solutions at third-party retail partner locations.
      - name: BrandsMart USA
        description: Aaron's Holdings subsidiary BrandsMart USA providing consumer electronics and appliance retail with lease-to-own financing.
      - name: Google Tag Manager
        description: Analytics and tracking integration via Google Tag Manager for website behavior analysis and marketing optimization.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
