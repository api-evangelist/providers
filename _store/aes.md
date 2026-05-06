---
aid: aes
url: https://raw.githubusercontent.com/api-evangelist/aes/refs/heads/main/apis.yml
name: AES Corporation
tags:
  - Energy
  - Power Generation
  - Renewable Energy
  - Battery Storage
  - Utility
  - Clean Energy
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
created: '2025-03-01'
modified: '2026-04-19'
description: The AES Corporation is a Fortune 500 global energy company that generates and distributes electrical power. AES operates a diverse portfolio of renewable, thermal, LNG, and battery storage facilities across multiple countries, serving utilities, industrial facilities, and end users. AES is the largest global supplier of clean energy to corporations in the Americas and operates 34.7 GW globally with $12.2 billion in annual revenue. The company serves 18.7 million household equivalents through utilities in Indiana, Ohio, and El Salvador. AES also co-founded Fluence Energy, a leading energy storage and software platform company.
specificationVersion: '0.16'
maintainers:
  - FN: API Evangelist
    url: http://apievangelist.com
    email: info@apievangelist.com
apis:
  - aid: aes:fluence-mosaic-api
    name: Fluence Mosaic API
    tags:
      - Energy Storage
      - Bidding
      - AI
      - Energy Markets
      - Software
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://fluenceenergy.com
    humanURL: https://fluenceenergy.com/software/mosaic/
    description: Mosaic is an AI-powered intelligent bidding application developed by Fluence (an AES and Siemens company) for optimizing energy market participation. Mosaic automates bidding strategies for battery energy storage systems in wholesale electricity markets, maximizing revenue through machine learning algorithms that analyze market prices, grid conditions, and storage asset capabilities.
    properties:
      - url: https://fluenceenergy.com/software/mosaic/
        type: Documentation
  - aid: aes:fluence-nispera-api
    name: Fluence Nispera API
    tags:
      - Asset Performance
      - Renewables
      - Operations
      - Software
      - Monitoring
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://fluenceenergy.com
    humanURL: https://fluenceenergy.com/software/nispera/
    description: Nispera is an asset performance management software platform by Fluence (an AES and Siemens company) for optimizing the performance of renewable energy and battery storage assets. Nispera provides monitoring, diagnostics, and analytics to help operators maximize energy yield and reduce O&M costs across solar, wind, and storage portfolios.
    properties:
      - url: https://fluenceenergy.com/software/nispera/
        type: Documentation
common:
  - url: https://www.aes.com/
    type: Portal
  - url: https://www.aes.com/about-aes
    type: Documentation
  - url: https://www.aes.com/newsroom
    type: Blog
  - url: https://www.aes.com/investors
    type: Portal
    title: Investor Relations
  - url: https://www.aes.com/careers
    type: Portal
    title: Careers
  - url: https://www.aes.com/legal
    type: TermsOfService
  - url: https://www.aes.com/privacy-policy
    type: PrivacyPolicy
  - url: https://www.aes.com/contact
    type: Contact
  - url: https://www.linkedin.com/company/aes-corporation/
    type: LinkedIn
  - url: https://fluenceenergy.com
    type: Portal
    title: Fluence Energy
  - type: Features
    data:
      - name: Carbon-Free Energy Supply
        description: AES is the largest global supplier of clean energy to corporations in the Americas, offering renewable energy from solar, wind, and hydro sources through long-term power purchase agreements.
      - name: Flexible Capacity
        description: Natural gas and LNG infrastructure providing reliable backup power and grid stability to complement intermittent renewable energy sources.
      - name: Battery Energy Storage
        description: Large-scale battery energy storage systems for grid stabilization, renewable integration, and energy arbitrage through Fluence, a joint venture with Siemens.
      - name: Grid Infrastructure
        description: Transmission, distribution, and digital solutions for optimizing electricity delivery networks across AES utility operations in the US and Latin America.
      - name: AI-Powered Operations
        description: Maximo, an AI-enabled solar installation robot, and AI safety platforms deployed across US operations to improve efficiency and reduce incident response time.
      - name: Fluence IQ Platform
        description: AI and machine learning digital platform developed by Fluence for intelligent asset optimization of energy storage and renewable generation facilities.
      - name: Energy Market Software
        description: Mosaic intelligent bidding application and Nispera asset performance management software enabling data-driven energy market participation and O&M optimization.
      - name: Regulated Utilities
        description: AES Indiana and AES Ohio provide regulated electric service to over 2.7 million customers with digital customer portals for account management.
  - type: UseCases
    data:
      - name: Corporate Renewable Energy Procurement
        description: Companies seeking carbon-free electricity through power purchase agreements with AES to meet sustainability goals and RE100 commitments.
      - name: Energy Storage for Grid Stability
        description: Utilities and grid operators deploying Fluence battery energy storage systems to balance supply and demand, provide frequency regulation, and integrate renewables.
      - name: Energy Market Revenue Optimization
        description: Storage asset owners using Fluence Mosaic to automate bidding in wholesale electricity markets and maximize revenue from battery storage resources.
      - name: Renewable Asset Performance Management
        description: Solar and wind operators using Fluence Nispera to monitor asset health, optimize energy yield, and reduce operations and maintenance costs.
      - name: Data Center Power
        description: Hyperscale technology companies partnering with AES for 24/7 carbon-free electricity to power data centers and meet sustainability commitments.
      - name: Industrial Decarbonization
        description: Industrial facilities transitioning from fossil fuels to renewable energy through AES clean energy supply agreements and behind-the-meter storage.
  - type: Integrations
    data:
      - name: Fluence Energy
        description: AES co-founded Fluence Energy with Siemens to provide leading energy storage products and software platforms including Mosaic and Nispera.
      - name: Google
        description: Partnership with Google for 24/7 renewable energy commitments supporting data center operations with carbon-free electricity.
      - name: Siemens
        description: Joint venture partner in Fluence Energy providing grid-scale battery storage systems and energy market optimization software.
      - name: MISO and PJM Markets
        description: Participation in Midcontinent and PJM wholesale electricity markets through AES Indiana and AES Ohio utility operations.
  - type: Solutions
    data:
      - name: AES Renewables
        description: Global clean energy development with 17.9 GW in operation and 67 GW in development, primarily solar and wind projects serving corporate and utility customers.
      - name: AES Energy Infrastructure
        description: Flexible thermal power plants and LNG infrastructure providing reliable capacity to complement renewable generation and support grid reliability.
      - name: AES Utilities
        description: AES Indiana and AES Ohio regulated electric utilities serving 2.7 million customers with digital customer portals and clean energy transition plans.
      - name: AES New Energy Technologies
        description: Innovation group developing next-generation energy solutions including AI-powered robotics, advanced energy storage, and grid modernization technologies.
---
