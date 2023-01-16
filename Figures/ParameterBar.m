subplot(5,1,1)
plotmeanbar(results, 2, 1:3, colors(1,:));
title('Width');

subplot(5,1,2)
plotmeanbar(results, 3, 1:4, colors(2,:));
title('Start Point');

subplot(5,1,3)
plotmeanbar(results, 4, 1:3, colors(3,:));
title('End Point');
ylabel('Average RRC')

subplot(5,1,4)
plotmeanbar(results, 5, 1:4, colors(4,:));
title('Angle');

subplot(5,1,5)
plotmeanbar(results, 6, 1:3, colors(5,:));
title('Offset');

set(gcf, 'position', [488.0000  117.0000  431.4000  741.0000])

function plotmeanbar(results, resultscol, values, color)
    meanslist = zeros(length(values), 1);
    minlist = zeros(length(values), 1);
    maxlist = zeros(length(values), 1);
    stdlist = zeros(length(values), 1);
    for i = 1:length(values)
        meanslist(i) = mean(results(find(results(:,resultscol)==values(i)), end-1));
        minlist(i) = min(results(find(results(:,resultscol)==values(i)), end-1));
        maxlist(i) = max(results(find(results(:,resultscol)==values(i)), end-1));
        stdlist(i) = std(results(find(results(:,resultscol)==values(i)), end-1));
    end

    bar(meanslist, 'FaceColor', color);
    hold on
    errorbar(values,meanslist,stdlist,stdlist, 'Color',...
            'k', 'LineWidth', 2, 'LineStyle', 'none');
    ylim([0 1.2]);
    my_defaults()
end