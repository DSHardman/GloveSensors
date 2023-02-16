my_colors;
load('morphologyData.mat');

figure();
my_errorbar({thickness}, colors(1,:));
ylim([1 1.25]);
my_defaults([328.2000  428.2000  384.8000  239.2000]);
ylabel('RRC');
set(gca,'XTick',[])

figure();
b = bar(0:0.2:1.2, shapes.', 'linewidth', 2);
b(1).FaceColor = colors(3,:);
b(2).FaceColor = colors(1,:);
my_defaults([661.0000  428.2000  645.6000  239.2000]);
ylim([1 1.25]);
ylabel('RRC');
set(gca,'XTick',[])