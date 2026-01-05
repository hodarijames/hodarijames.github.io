# ISLANDS Lab Website

A clean, professional website for the ISLANDS (Interstellar Search for Life Around Nearby Dwarf Stars) research group at Agnes Scott College.

## Quick Start

This website is designed to be deployed to GitHub Pages. Here's how to get it up and running:

### 1. Set Up Your GitHub Repository

If you're replacing your existing hodarijames.github.io site:
1. Go to your existing hodarijames.github.io repository on GitHub
2. Delete all existing files (or back them up first!)
3. Upload all files from this `islands-site` folder

If starting fresh:
1. Create a new repository named `hodarijames.github.io`
2. Upload all files from this `islands-site` folder

### 2. Add Your Images

You'll need to create an `images` folder and add these files:
- `Islands_logo_official.png` (your logo - already have this!)
- `hshj_headshot.jpg` (your headshot)
- `lines_benchmark.png` (from your current site)
- `ha_li_20pc_both.png` (from your current site)  
- `FeH_Teff_Exo_20pc_border.png` (from your current site)

Copy these images from your current website to keep everything working.

### 3. Enable GitHub Pages

1. Go to your repository Settings
2. Navigate to "Pages" in the left sidebar
3. Under "Source", select "Deploy from a branch"
4. Choose "main" branch and "/ (root)" folder
5. Click Save

Your site will be live at `https://hodarijames.github.io` within a few minutes!

## Customization Guide

### Adding News Items

Edit `index.html`, find the "Lab News" section, and add new items:

```html
<div class="news-item">
    <span class="news-date">Month Year:</span>
    <span class="news-content">Description of news...</span>
</div>
```

### Adding Publications

Edit `publications.html`. For published papers, use this format:

```html
<div class="publication">
    <p class="pub-authors">Author, A., Hubbard-James, H.-S., & Coauthor, C.</p>
    <p class="pub-title">Paper Title</p>
    <p class="pub-details">
        Journal Name, Volume, Page (Year) 
        <a href="https://doi.org/..." class="pub-link" target="_blank">DOI</a>
    </p>
</div>
```

### Adding Student Researchers

Edit `people.html`, find the "Student Researchers" section, and add:

```html
<div class="person-card">
    <div class="person-image">
        <img src="images/student_name.jpg" alt="Student Name">
    </div>
    <div class="person-info">
        <h3>Student Name</h3>
        <p class="person-title">Undergraduate Researcher</p>
        <p class="person-bio">
            Brief description of their research and interests...
        </p>
    </div>
</div>
```

### Changing Colors

The main accent color is teal (`#2c7a7b`). To change it, edit `style.css` and search for `#2c7a7b` - replace all instances with your preferred color code.

### Linking to Your Spectral Library

The site currently links to `spectral_library/page1.html`. Make sure this tool is accessible at that path, or update the links in:
- `publications.html`
- `resources.html`

## File Structure

```
islands-site/
├── index.html           # Homepage
├── research.html        # Research page
├── people.html          # People page
├── publications.html    # Publications page
├── resources.html       # Resources page
├── style.css           # Main stylesheet
├── images/             # Images folder (you need to create this)
│   ├── Islands_logo_official.png
│   ├── hshj_headshot.jpg
│   └── [research images]
└── README.md           # This file
```

## Features

- **Responsive Design**: Works on desktop, tablet, and mobile
- **Lab-Focused Branding**: Professional research group identity
- **Clean Navigation**: Easy to find information
- **No Monthly Fees**: Free hosting on GitHub Pages
- **Easy to Update**: Simple HTML/CSS structure

## Next Steps

1. **Content Review**: Go through each page and update any placeholder text
2. **Add Images**: Place all required images in the `images/` folder
3. **Update CV Link**: Add your CV PDF and update the link in `people.html`
4. **Test Navigation**: Make sure all internal links work correctly
5. **Custom Domain** (Optional): You can add a custom domain in GitHub Pages settings

## Need Help?

If you want to make more extensive changes:
- **Option 1**: Edit the HTML/CSS files directly (they're straightforward!)
- **Option 2**: Hire someone on Fiverr to customize (~$50-200)
- **Option 3**: Migrate to Squarespace (but you'll pay monthly fees)

The beauty of this setup is that it's free forever and you own all the files!

## Updates Log

- December 2025: Initial ISLANDS Lab website created
  - Lab-focused structure
  - Professional design inspired by modern research group sites
  - Mobile-responsive layout
  - Zero ongoing costs
