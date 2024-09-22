#!/bin/bash


echo ""
echo "INSTALLING DEPENDENCIES required for GUI..."
echo ""

# Check for Homebrew, install if we don't have it
if test ! $(which brew); then
    echo "Installing Homebrew..."
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    echo ''
fi

 (echo; echo 'eval "$(/usr/local/bin/brew shellenv)"') >> /Users/admin/.zprofile
    eval "$(/usr/local/bin/brew shellenv)"

echo ""
echo "Installing ADB Platform Tool..."
brew install --cask android-platform-tools
echo ""

echo ""
echo "Installing Pillow..."
pip3 install pillow
echo ""

echo ""
echo "Installing Depends..."
pip install depends
echo ""


echo ""
echo "Dependencies installed!!!"
echo ""


exit 1
