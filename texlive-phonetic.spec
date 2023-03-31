Name:		texlive-phonetic
Version:	56468
Release:	2
Summary:	MetaFont Phonetic fonts, based on Computer Modern
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/phonetic
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/phonetic.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/phonetic.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The fonts are based on Computer Modern, and specified in
MetaFont. Macros for the fonts' use are provided, both for
LaTeX 2.09 and for current LaTeX.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/source/public/phonetic
%{_texmfdistdir}/fonts/tfm/public/phonetic
%{_texmfdistdir}/tex/latex/phonetic
%doc %{_texmfdistdir}/doc/fonts/phonetic

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
