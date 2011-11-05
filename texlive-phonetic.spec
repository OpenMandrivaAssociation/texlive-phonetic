# revision 21871
# category Package
# catalog-ctan /fonts/phonetic
# catalog-date 2011-03-28 22:21:58 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-phonetic
Version:	20110328
Release:	1
Summary:	MetaFont Phonetic fonts, based on Computer Modern
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/phonetic
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/phonetic.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/phonetic.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The fonts are based on Computer Modern, and specified in
MetaFont. Macros for the fonts' use are provided, both for
LaTeX 2.09 and for current LaTeX.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/source/public/phonetic/cmph10.mf
%{_texmfdistdir}/fonts/source/public/phonetic/cmph5.mf
%{_texmfdistdir}/fonts/source/public/phonetic/cmph6.mf
%{_texmfdistdir}/fonts/source/public/phonetic/cmph7.mf
%{_texmfdistdir}/fonts/source/public/phonetic/cmph8.mf
%{_texmfdistdir}/fonts/source/public/phonetic/cmph9.mf
%{_texmfdistdir}/fonts/source/public/phonetic/cmphb10.mf
%{_texmfdistdir}/fonts/source/public/phonetic/cmphi10.mf
%{_texmfdistdir}/fonts/source/public/phonetic/cmphi7.mf
%{_texmfdistdir}/fonts/source/public/phonetic/cmphi8.mf
%{_texmfdistdir}/fonts/source/public/phonetic/cmphi9.mf
%{_texmfdistdir}/fonts/source/public/phonetic/local.mf
%{_texmfdistdir}/fonts/source/public/phonetic/phochar.mf
%{_texmfdistdir}/fonts/source/public/phonetic/phoital.mf
%{_texmfdistdir}/fonts/source/public/phonetic/phoitchar.mf
%{_texmfdistdir}/fonts/source/public/phonetic/phosym.mf
%{_texmfdistdir}/fonts/source/public/phonetic/symchar.mf
%{_texmfdistdir}/fonts/tfm/public/phonetic/cmph10.tfm
%{_texmfdistdir}/fonts/tfm/public/phonetic/cmph5.tfm
%{_texmfdistdir}/fonts/tfm/public/phonetic/cmph6.tfm
%{_texmfdistdir}/fonts/tfm/public/phonetic/cmph7.tfm
%{_texmfdistdir}/fonts/tfm/public/phonetic/cmph8.tfm
%{_texmfdistdir}/fonts/tfm/public/phonetic/cmph9.tfm
%{_texmfdistdir}/fonts/tfm/public/phonetic/cmphb10.tfm
%{_texmfdistdir}/fonts/tfm/public/phonetic/cmphi10.tfm
%{_texmfdistdir}/fonts/tfm/public/phonetic/cmphi7.tfm
%{_texmfdistdir}/fonts/tfm/public/phonetic/cmphi8.tfm
%{_texmfdistdir}/fonts/tfm/public/phonetic/cmphi9.tfm
%{_texmfdistdir}/tex/latex/phonetic/Uphon.fd
%{_texmfdistdir}/tex/latex/phonetic/phonetic.sty
%doc %{_texmfdistdir}/doc/fonts/phonetic/Doc/209/phonetic-table.tex
%doc %{_texmfdistdir}/doc/fonts/phonetic/Doc/209/phonetic.sty
%doc %{_texmfdistdir}/doc/fonts/phonetic/Doc/README
%doc %{_texmfdistdir}/doc/fonts/phonetic/README
%doc %{_texmfdistdir}/doc/fonts/phonetic/makefile
%doc %{_texmfdistdir}/doc/fonts/phonetic/phonetic-table.pdf
%doc %{_texmfdistdir}/doc/fonts/phonetic/phonetic-table.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
