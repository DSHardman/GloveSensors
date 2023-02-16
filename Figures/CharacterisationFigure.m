load('characterisationData.mat');
load("../StrainTests/AllCroppedStrains.mat");

t = tiledlayout(2,2);
t.TileSpacing = 'compact';
t.Padding = 'compact';
my_colors();

nexttile;
x = 0:4:20;
fill([x fliplr(x)], [rawvals(1,:) fliplr(rawvals(3,:))], colors(1,:), 'FaceAlpha', 0.5, 'EdgeColor', 'none');
hold on
plot(x, rawvals.', 'color', 'k', 'linewidth', 2);
hold on
line([10 10], [1 1000], 'color', 'k', 'LineWidth', 2, 'LineStyle', '--');
my_defaults();
set(gca, 'YScale', 'log');
xlabel('Salt (wt %)');
ylabel('Resistance (k\Omega)');

nexttile;
x = 0:10:50;
fill([x fliplr(x)], [cornflour(1,:) fliplr(cornflour(6,:))], colors(2,:), 'FaceAlpha', 0.5, 'EdgeColor', 'none');
hold on
plot(x, cornflour.', 'color', 'k', 'linewidth', 2);
hold on
my_defaults();
set(gca, 'YScale', 'log');
xlabel('Cornflour (wt %)');
ylabel('Resistance (k\Omega)');
xlim([0 50]);

nexttile;
plot(nan, nan, 'linewidth', 2, 'color', colors(3,:));
hold on
plot(nan, nan, 'linewidth', 2, 'color', colors(5,:));

addsample(s4, 105, colors(5,:));
addsample(s5, 103, colors(5,:));
addsample(s11, 112, colors(5,:));
addsample(s1, 107, colors(3,:));
addsample(s2, 105, colors(3,:));
addsample(s3, 108, colors(3,:));
addsample(s8, 110, colors(3,:));
my_defaults();
xlabel('Strain (%)');
ylabel('\Delta R/R_0');
legend({'New'; 'Old'}, 'FontSize', 15, 'location', 'se');
legend boxoff

nexttile;
addtrap(s6(5:292), colors(1,:));
hold on
addtrap(s7(5:292), colors(2,:));
% addtrap(s9(1:300), 'r');
% addtrap(s10(1:300), 'r');
my_defaults([362.6000  323.4000  870.4000  469.6000]);
xlabel('Time (s)');
ylabel('\Delta R/R_0');
legend({'30%';'100%'}, 'FontSize', 15, 'location', 'n', 'orientation', 'horizontal');
legend boxoff
ylim([0.8 5]);
xlim([0 70]);


function addsample(s, l, color)
    scale = 0.4831; %% mm per reading
    plot((100*scale/l)*(0:(length(s)-1)), s./s(1), 'color', color, 'LineWidth', 2);
    hold on
    scatter((100*scale/l)*(length(s)-1), s(end)/s(1), 30, color, 'marker', 'x', 'LineWidth', 2);
end

function addtrap(s, color)
    scale = 0.2440; %% s per reading
    plot(scale*(0:(length(s)-1)), s./s(1), 'color', color, 'LineWidth', 2);
end