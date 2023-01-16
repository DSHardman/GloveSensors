medians = zeros(41,1);
means = zeros(41,1);

for i = 5:45
    medians(i-4) = median(results(i-4:i, end-1));
    means(i-4) = mean(results(i-4:i, end-1));
end

plot(5:45, means, 'color', colors(1,:), 'LineWidth', 4);
hold on;
plot(5:45, medians, 'color', colors(2,:), 'LineWidth', 4);
xlim([5 45]);
ylim([0.4 0.9]);
my_defaults([248.2000  429.8000  852.8000  428.2000]);
set(gca, 'FontSize', 25)
legend({'Rolling Mean';'Rolling Median'}, 'orientation', 'vertical',...
    'location', 'ne', 'Fontsize', 25);
legend boxoff
ylabel('RRC');
xlabel('Iterations');