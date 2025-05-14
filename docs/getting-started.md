# Getting Started with CherryBomb

This guide will walk you through the process of installing CherryBomb, setting up your first project, and beginning your social media data analysis journey.

## System Requirements

- **Operating Systems**: Windows 10+ / macOS 10.15+ / Ubuntu 18.04+
- **RAM**: 8GB minimum (16GB recommended for larger datasets)
- **Storage**: 500MB for application + storage for datasets (varies based on usage)
- **Internet**: Broadband connection required for data collection

## Installation

### macOS

1. Download the latest CherryBomb.dmg from our [releases page](https://github.com/seamusmullan/CherryBomb/releases)
2. Open the .dmg file and drag CherryBomb to your Applications folder
3. Launch CherryBomb from your Applications folder

### Windows

1. Download the latest CherryBomb-Setup.exe from our [releases page](https://github.com/seamusmullan/CherryBomb/releases)
2. Run the installer and follow the on-screen instructions
3. Launch CherryBomb from the Start menu

### Linux

```bash
# Add our PPA
sudo add-apt-repository ppa:cherrybomb/stable
sudo apt update

# Install CherryBomb
sudo apt install cherrybomb-desktop
```

## First-Time Setup

When you first launch CherryBomb, you'll be guided through a setup wizard:

1. **Create Account**: Set up your CherryBomb account for cloud syncing (optional)
2. **Connect Platforms**: Authorize CherryBomb to access your social media accounts
3. **Choose Data Location**: Select where your scraped data will be stored

## Creating Your First Project

1. From the dashboard, click "New Project"
2. Enter a name and description for your project
3. Select the social media platforms you want to analyze
4. Choose accounts to scrape (your own or others that are public)
5. Configure scraping settings:
   - Data points to collect
   - Historical time range
   - Update frequency

## Collecting Your First Dataset

1. In your project, navigate to the "Data Collection" tab
2. Click "Start Collection" to begin scraping the selected accounts
3. Monitor progress in the "Collection Status" panel
4. Once complete, your data will be processed and prepared for analysis

## Viewing Initial Insights

1. Go to the "Dashboard" tab to see an overview of your collected data
2. Explore visualizations showing engagement trends, posting patterns, and audience activity
3. Navigate to "Analysis" for more detailed metrics and comparisons

## Creating Your First Prediction

1. Navigate to the "Prediction" tab
2. Click "New Prediction"
3. Upload or create draft content you're considering posting
4. Select which metrics you want to predict (likes, shares, comments, etc.)
5. Click "Generate Prediction" to see forecasted performance metrics

## Next Steps

- Learn about [Dataset Management](core-concepts/dataset-management.md) to organize your data
- Explore [Trend Analysis](core-concepts/trend-analysis.md) to identify patterns
- Understand [Prediction Models](core-concepts/prediction-models.md) to optimize future content
