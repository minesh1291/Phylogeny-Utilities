#!/usr/bin/perl
use strict;

if(@ARGV!=2){print "USAGE:\n\tperl $0 <Infile> <Outfile>\n";exit;}

my$infile=$ARGV[0];
my$outfile=$ARGV[1];
open(FH,$infile);
my@cont=<FH>;
close(FH);
my$cont=join('',@cont);
$cont=~s/\)/)\n/g;
@cont=split("\n",$cont);
open(FHout,'>'.$outfile)or die $!;
foreach my$line (@cont){
	if($line=~/^:(\d+\.\d+)(.*)/){
		my$boot=$1;
		my$tail=$2;
		print FHout $line=$boot.":1".$tail;
		}else{
			print FHout $line;
			}
}
close(FHout);
